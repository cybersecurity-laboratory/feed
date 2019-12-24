# what's this?
This is an IoCs that has been molded to be easily incorporated into Netwitness Feeds and Lists.
The latest list contains the latest IOC at the moment. The old emotet may not be covered, but the query is simplified so you can get the most out of Netwitness.
The composit list summarizes the IOCs identified so far. This is covered wide detection range but an error occurs in some operations of Netwitness, because too mane long query.

Thanks to @cryptolaemus1 for providing the original IoC.

#### composit_domain and composit_ip

Contains all the information since this feed went live. That least likely to miss a threat. However, it does not work with Netwitness10.x because the query is too many long. It works on Netwitness11.x, but fails on PDF export and Investigate.
Therefore, this list can only be used to check the report visually. It will help shape Investigate's policy.

#### latest_domain and latest_ip
