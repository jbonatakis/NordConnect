# NordVPN Server Load Analyzer

A program to determine which NordVPN server is currently under the lightest load.
This project inspired by: https://github.com/mrzool/nordvpn-server-find

![server-load](https://raw.githubusercontent.com/jbonatakis/vpn-server-load/master/pictures/server-load.png)
### Requirements
* Python 3


### Setup
This program should not require any additional setup. Simply clone the repository or download the python file and run it.


### Directions
To use the program, run:

`python3 server_load.py <country code> <number of servers>`


Replace `<country code>` above with one of the following country codes below:


    'ad' 'ae' 'af' 'ag' 'ai' 'al' 'am' 'ao' 'aq' 'ar' 'as' 'at' 'au' 'aw' 'ax'
    'az' 'ba' 'bb' 'bd' 'be' 'bf' 'bg' 'bh' 'bi' 'bj' 'bl' 'bm' 'bn' 'bo' 'bq'
    'br' 'bs' 'bt' 'bv' 'bw' 'by' 'bz' 'ca' 'cc' 'cd' 'cf' 'cg' 'ch' 'ci' 'ck'
    'cl' 'cm' 'cn' 'co' 'cr' 'cu' 'cv' 'cw' 'cx' 'cy' 'cz' 'de' 'dj' 'dk' 'dm'
    'do' 'dz' 'ec' 'ee' 'eg' 'eh' 'er' 'es' 'et' 'fi' 'fj' 'fk' 'fm' 'fo' 'fr'
    'ga' 'gb' 'gd' 'ge' 'gf' 'gg' 'gh' 'gi' 'gl' 'gm' 'gn' 'gp' 'gq' 'gr' 'gs'
    'gt' 'gu' 'gw' 'gy' 'hk' 'hm' 'hn' 'hr' 'ht' 'hu' 'id' 'ie' 'il' 'im' 'in'
    'io' 'iq' 'ir' 'is' 'it' 'je' 'jm' 'jo' 'jp' 'ke' 'kg' 'kh' 'ki' 'km' 'kn'
    'kp' 'kr' 'kw' 'ky' 'kz' 'la' 'lb' 'lc' 'li' 'lk' 'lr' 'ls' 'lt' 'lu' 'lv'
    'ly' 'ma' 'mc' 'md' 'me' 'mf' 'mg' 'mh' 'mk' 'ml' 'mm' 'mn' 'mo' 'mp' 'mq'
    'mr' 'ms' 'mt' 'mu' 'mv' 'mw' 'mx' 'my' 'mz' 'na' 'nc' 'ne' 'nf' 'ng' 'ni'
    'nl' 'no' 'np' 'nr' 'nu' 'nz' 'om' 'pa' 'pe' 'pf' 'pg' 'ph' 'pk' 'pl' 'pm'
    'pn' 'pr' 'ps' 'pt' 'pw' 'py' 'qa' 're' 'ro' 'rs' 'ru' 'rw' 'sa' 'sb' 'sc'
    'sd' 'se' 'sg' 'sh' 'si' 'sj' 'sk' 'sl' 'sm' 'sn' 'so' 'sr' 'ss' 'st' 'sv'
    'sx' 'sy' 'sz' 'tc' 'td' 'tf' 'tg' 'th' 'tj' 'tk' 'tl' 'tm' 'tn' 'to' 'tr'
    'tt' 'tv' 'tw' 'tz' 'ua' 'ug' 'uk' 'um' 'us' 'uy' 'uz' 'va' 'vc' 've' 'vg'
    'vi' 'vn' 'vu' 'wf' 'ws' 'ye' 'yt' 'za' 'zm' 'zw'

Country code is required for the program to run.


Replace `<number of servers>` with the number of servers you wish the program to return. If no value is given, the program will default to 10 servers.
