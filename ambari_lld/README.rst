============================
Ambari alerts LLD for Zabbix
============================

This program connects to the Ambari server API and returns all the alerts
associated to a given host as a JSON that can be easily parsed by Zabbix
to create Low-Level-Discovered items.

Usage::

  usage: ambari_zabbix_lld [-h] [-a AMBARI_ENDPOINT] [-u USER] [-p PASSWORD]
                  [-n HOSTNAME]

  Return a Zabbix LLD JSON resource for all available Ambari checks

  optional arguments:
    -h, --help            show this help message and exit
    -a AMBARI_ENDPOINT, --ambari-endpoint AMBARI_ENDPOINT
                          Ambari API address
    -u USER, --user USER  Ambari user
    -p PASSWORD, --password PASSWORD
                          Ambari user password
    -n HOSTNAME, --hostname HOSTNAME
                          Filter alerts based on this hostname

By default ``-n`` has a value of ``*`` which means that no filters are 
applied to hostnames. You can pass an empty string if you want to retrieve
alerts that are not assigned to any particular host. Obviously you can
(and probably want to) pass an hostname to filter only relevant alerts.

The ``AMBARI_ENDPOINT`` URI must always begin with ``http(s)://``.

