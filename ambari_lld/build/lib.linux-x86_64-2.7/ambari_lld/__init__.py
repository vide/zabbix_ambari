#!/usr/bin/env python

import argparse
import json
import requests

AMBARI_API = {}

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Return a Zabbix LLD JSON resource for all available Ambari checks')
    parser.add_argument('-a', '--ambari-endpoint', help='Ambari API address',
                        default='http://localhost:8080')
    parser.add_argument('-u', '--user', help='Ambari user', default='admin')
    parser.add_argument('-p', '--password', help='Ambari user password', default='admin')
    parser.add_argument('-n', '--hostname',
                        help='Filter alerts based on this hostname', default='*')

    return parser.parse_args()

def get_alerts(cluster_name, hostname_filter):
    """
    Return a JSON with all the alarm assigned to a given host. Empty hostname
    filters only the cluster-wide alerts (not connected to specific hostname). If you
    want the whole list, pass '*' as hostname_filter
    """
    filtered_alerts = []
    url = "%s/clusters/%s/alerts" % (AMBARI_API["url"], cluster_name)
    alerts = requests.get(url, headers=AMBARI_API["headers"], auth=AMBARI_API["auth"]).json()
    for alert in alerts["items"]:
        if (alert["Alert"]["host_name"] == hostname_filter) \
           | (hostname_filter == '*') \
           | ((hostname_filter == "") & (alert["Alert"]["host_name"] is None)):
            filtered_alerts.append(alert)
    return filtered_alerts

def get_cluster_name():
    u"""
    Return the first cluster name in this ambari instance. We naively assume that
    there is just one cluster per ambari
    """
    url = "%s/clusters/" % (AMBARI_API["url"])
    cluster_info = requests.get(url, headers=AMBARI_API["headers"], auth=AMBARI_API["auth"])
    return cluster_info.json()["items"][0]["Clusters"]["cluster_name"]

def print_lld_json(alerts=[]):
    """
    Return the LLD JSON for Zabbix to process
    Check https://www.zabbix.com/documentation/3.2/manual/discovery/low_level_discovery
    for reference
    """
    lld_json = {}
    lld_json["data"] = []
    for alert in alerts:
        lld = {}
        lld["{#AMAL_URL}"] = alert["href"]
        lld["{#AMAL_NAME}"] = alert["Alert"]["definition_name"]
        lld["{#AMAL_SVC}"] = alert["Alert"]["service_name"]
        lld["{#AMAL_HOSTNAME}"] = alert["Alert"]["host_name"]
        lld_json["data"].append(lld)
    print json.dumps(lld_json, indent=4, sort_keys=True)

def main():
    '''Entry point if called as an executable'''
    global AMBARI_API
    args = parse_arguments()
    AMBARI_API["url"] = "%s/api/v1" % (args.ambari_endpoint)
    AMBARI_API["headers"] = {'X-Requested-By': 'ambari'}
    AMBARI_API["auth"] = (args.user, args.password)
    hdp_cluster = get_cluster_name()
    print_lld_json(alerts=get_alerts(hdp_cluster, args.hostname))

if __name__ == '__main__':
    main()
