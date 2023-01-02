dictionaries with scan display:
urls are links from sanskrit-lexicon homepage at Cologne.

+ pwg https://sanskrit-lexicon.uni-koeln.de/pwgindex.html
+ pw https://sanskrit-lexicon.uni-koeln.de/pwindex.html

+ wil https://sanskrit-lexicon.uni-koeln.de/scans/WILScan/index.php?sfx=jpg
  sfx parameter not used.
+ md https://sanskrit-lexicon.uni-koeln.de/scans/MDScan/index.php?sfx=jpg
  sfx parameter not used.
+ cae https://sanskrit-lexicon.uni-koeln.de/scans/CAEScan/index.php?sfx=png
  sfx parameter not used.
+ ccs https://sanskrit-lexicon.uni-koeln.de/scans/CCSScan/index.php?sfx=png
  sfx parameter not used.
+ sch https://sanskrit-lexicon.uni-koeln.de/scans/SCHScan/index.php
+ pgn https://sanskrit-lexicon.uni-koeln.de/scans/PGNScan/2014/webscan/index.php
  No changes made. Depends on web/webtc/servepdf.php.
+ ae https://sanskrit-lexicon.uni-koeln.de/scans/AEScan/index.php?sfx=pdf
+ ae https://sanskrit-lexicon.uni-koeln.de/scans/AEScan/index.php?sfx=jpg
+ mw https://sanskrit-lexicon.uni-koeln.de/scans/MWScan/index.php?sfx=pdf
+ mw       https://sanskrit-lexicon.uni-koeln.de/scans/MWScan/index.php?sfx=jpg

+ stc https://sanskrit-lexicon.uni-koeln.de/scans/STCScan/index.php?sfx=jpg
  sfx not used
stc https://sanskrit-lexicon.uni-koeln.de/scans/STCScan/web/index_fr.php


Save original versions of the scanned edition code for dictionary xxx into
subdirectory xxx/orig/
sh step0.sh

payload: ><img src=a onerror=prompt('xss')>

%22%3E%3Cimg%20src=a%20onerror=prompt(%27xss%27)%3E

-------------------------------------------------------------
cgi-bin
/nfs/projekt/sanskrit-lexicon/http/cgi/
 serveimg.pl -> serveimg.perl
 https://www.sanskrit-lexicon.uni-koeln.de/cgi-bin/work/wilscan/serveimg.pl

