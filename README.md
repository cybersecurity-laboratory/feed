# Feed
[![Build Status](https://travis-ci.org/netwitness999/feed.svg?branch=master)](https://travis-ci.org/netwitness999/feed)

Netwitness Custom Feedsから参照するためのFeedです.

NetWitnessには外部のリストを取り込んで独自のメタデータ（タグ）を付ける機能があります
Configure > Custom Feeds で設定できます
上記のURLから取り込んだデータをもとに ir.general = "black_listed" というメタデータを付けています
これによって、いちいちNetWitnessを触ることなく、危険なURLを NetWitness に取り込めるようにしています
 
したがって、Githubにアカウントを持っている方にお願いしたいのは以下の作業です
 
1. netwitness999/feed リポジトリの Issues にブラックリスト登録依頼が上がっていないかチェックしてください
https://github.com/cybersecurity-laboratory/feed/issues

2. 上がってる場合は blacklisted_domain か blacklisted_ip を更新してください

https://github.com/cybersecurity-laboratory/feed/blob/master/blacklisted_domain_extend
https://github.com/cybersecurity-laboratory/feed/blob/master/blacklisted_ip_extend

3. 更新し終えたら該当のIssuesをクローズしてください
