<?php
 $sfx = $_GET['sfx'];
 // for pdf, directory is relative to this 'xxview' directory;
 // for images, directory use relative to that of ../serveimg.pl
 // 11-28-2022 Deactivate jpg display.
 $sfx = "pdf";
 if ($sfx == "pdf"){
  $dir="/scans/MWScan/MWScan" . $sfx . "/";
 }
 else {
  $dir="/scans/MWScan/MWScan" . $sfx . "/";
 }
function output_item ($dir,$sfx,$filename,$word,$pagenum) {
    $outfile=$dir . $filename . "." . $sfx;
    echo "$pagenum";
    echo "&nbsp;&nbsp;";
    if ($sfx == "pdf") {
     echo "<a href=\"$outfile\"";
    } else { //if ($sfx == "jpg")
    // Could write a php version of serveimg.pl
   // 11-28-2022 deactivate
   //echo "<a href=\"/cgi-bin/serveimg.pl?file=$outfile\"";

/* the following generates an image on the fly. It is more versatile,
  but the creation time is noticeable.
     $infile="../MWScan/MWScan/" . $filename . "." .  "tif";
     $resize="1000x1500";
     echo "<a href=\"serveimgAlt.pl?file=$infile&resize=$resize\"";
*/
    }
    echo " target=\"output\">$word</a>";
    echo "<br />";
    echo "\n";
 }
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "//www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="//www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <title>MW Scan Input Form</title>
    <link rel="stylesheet" href="/css/main.css">
  </head>
  <body>
<p>
  <img id="unilogo" src="/images/unilogo.gif"
   alt="University of Cologne" width="32" height="52" />
  <img id="shield" src="/images/shield.png"
     alt="Brown University" width="32" height="52" />
<h2>Monier-Williams Sanskrit Dictionary Scanned Images</h2>
</p>
<a id="top"></a>
<a href=#preface>PREFACE</a> <br />
<a href=#supplement>SUPPLEMENT</a> <br />
<div id="words">
<p>
<?php
 $filename="mwfiles.txt";
 $file=fopen($filename,"r") or exit("Unable to open file $filename");
 $n = 0;
 $m = 9999; // make smaller for testing
 $pattern='/^mw([0-9]+)-([a-zA-Z]+)$/';
 while(((!feof($file)) && ($n < $m))) {
   $n++;
   $line = fgets($file);
   if (preg_match($pattern,$line,$matches)) {
    $reffile=$matches[0];
    $word = $matches[2];
    $pagenum= $matches[1];
    output_item($dir,$sfx,$reffile,$word,$pagenum);
   }
  }

 fclose($file);
?>
</p>
</div>


<div>
<a id="supplement"><h2>Supplement: Additions and Corrections</h2></a> 
 (<a href=#top>back to top</a> )<br />
<?php
// output_item($dir,$sfx,"ae-vor-01","Title","");

output_item($dir,$sfx,"mw1308-hvala","aMSarUpiNI","");
output_item($dir,$sfx,"mw1309","agRhIta","");
output_item($dir,$sfx,"mw1310","atisvinna","");
output_item($dir,$sfx,"mw1311","anaka","");
output_item($dir,$sfx,"mw1312","anunadi","");
output_item($dir,$sfx,"mw1313","antara","");
output_item($dir,$sfx,"mw1314","apamud","");
output_item($dir,$sfx,"mw1315","abjala","");
output_item($dir,$sfx,"mw1316","ambujinI","");
output_item($dir,$sfx,"mw1317","avagraha","");
output_item($dir,$sfx,"mw1318","aSvaka","");
output_item($dir,$sfx,"mw1319","AkiMcanya","");
output_item($dir,$sfx,"mw1320","Amredita-yamaka","");
output_item($dir,$sfx,"mw1321","indrANI","");
output_item($dir,$sfx,"mw1322","udgAla","");
output_item($dir,$sfx,"mw1323","Rtavya-vat","");
output_item($dir,$sfx,"mw1324","kapilAhvaya","");
output_item($dir,$sfx,"mw1325","kuTvudI","");
output_item($dir,$sfx,"mw1326","khaDgaka","");
output_item($dir,$sfx,"mw1327","catur","");
output_item($dir,$sfx,"mw1328","jhaTiti","");
output_item($dir,$sfx,"mw1329","dIpta","");
output_item($dir,$sfx,"mw1330","notseka","");
output_item($dir,$sfx,"mw1331","preShyAntevAsin","");
output_item($dir,$sfx,"mw1332","raSmi-dhAra","");
output_item($dir,$sfx,"mw1333","sarSapa-miSra","");
?>
</div>

<div>
<a id="preface"><h2>Preface</h2></a> 
 (<a href=#top>back to top</a>)<br />
<p>
<?php
// output_item($dir,$sfx,"ae-vor-01","Title","");
output_item($dir,$sfx,"mw010001","Title","");
output_item($dir,$sfx,"mw010002","Copyright","");
output_item($dir,$sfx,"mw010007","Title","");
output_item($dir,$sfx,"mw010008","Publisher","");
output_item($dir,$sfx,"mw010009","Page v: Preface","");
output_item($dir,$sfx,"mw010010","Page vi","");
output_item($dir,$sfx,"mw010011","Page vii","");
output_item($dir,$sfx,"mw010012","Page viii","");
output_item($dir,$sfx,"mw010013","Page ix","");
output_item($dir,$sfx,"mw010014","Page x: Postscript","");
output_item($dir,$sfx,"mw010015","Page xi: Introduction Section I","");
output_item($dir,$sfx,"mw010016","Page xii","");
output_item($dir,$sfx,"mw010017","Page xiii","");
output_item($dir,$sfx,"mw010018","Page xiv: Section II","");
output_item($dir,$sfx,"mw010019","Page xv","");
output_item($dir,$sfx,"mw010020","Page xvi","");
output_item($dir,$sfx,"mw010021","Page xvii","");
output_item($dir,$sfx,"mw010022","Page xviii","");
output_item($dir,$sfx,"mw010023","Page xix","");
output_item($dir,$sfx,"mw010024","Page xx: Section III","");
output_item($dir,$sfx,"mw010025","Page xxi","");
output_item($dir,$sfx,"mw010026","Page xxii: Section IV","");
output_item($dir,$sfx,"mw010027","Page xxiii","");
output_item($dir,$sfx,"mw010028","Page xxiv","");
output_item($dir,$sfx,"mw010029","Page xxv","");
output_item($dir,$sfx,"mw010030","Page xxvi","");
output_item($dir,$sfx,"mw010031","Page xxvii","");
output_item($dir,$sfx,"mw010032","Page xxviii","");
output_item($dir,$sfx,"mw010034","Page xxix","");
output_item($dir,$sfx,"mw010033","Page xxx","");
output_item($dir,$sfx,"mw010035","Page xxxi","");
output_item($dir,$sfx,"mw010036","Page xxxii","");
output_item($dir,$sfx,"mw010005","Page xxxiii: Works","");
output_item($dir,$sfx,"mw010006","Page xxxiv ","");
output_item($dir,$sfx,"mw010004","Page xxxv: Abbreviations","");
output_item($dir,$sfx,"mw010003","Page xxxvi: Dict. Order","");
?>
</p>
</div>

</body>
</html>
