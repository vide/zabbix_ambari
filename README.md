## Ambari integration with Zabbix LLD

This small repo helps you integrating Zabbix with Ambari built-in alerts
so, if you are a Zabbix user, you can centralize notifications & escalations 
in one central place.

`zbx_ambari_lld_template.xml` is a Zabbix exported template that you need to
import in Zabbix to create the LLD rules

`userparameter_ambari_alerts.conf` is a sample implementation of the items the
aforementioned template relies on.

Finally, in `ambari_lld` there's a small [Python package that you can install with `pip`](https://pypi.python.org/pypi/ambari-lld) that is in turn used by the autodiscovery user parameter.

If you find any bug or want to implement something new, please open a PR!
