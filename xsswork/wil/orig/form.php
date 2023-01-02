<?php
 $sfx = $_GET['sfx'];
 // for pdf, directory is relative to this 'xxview' directory;
 // for images, directory use relative to that of ../serveimg.pl
 if ($sfx == "pdf"){
  $dir="/scans/WILScan/WILScan" . $sfx . "/";
 }
 else {
  $dir="/scans/WILScan/WILScan" . $sfx . "/";
 }
function output_item ($dir,$sfx,$filename,$word,$pagenum) {
    $outfile=$dir . $filename . "." . $sfx;
    echo "$pagenum";
    echo "&nbsp;&nbsp;";
    if ($sfx == "pdf") {
     echo "<a href=\"$outfile\"";
    } else { //if ($sfx == "jpg") or "png"
     echo "<a href=\"/cgi-bin/serveimg.pl?file=$outfile\"";
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
    <title>WIL Scan Input Form</title>
    <link rel="stylesheet" href="/css/main.css">
<p>
  <img id="unilogo" src="/images/unilogo.gif"
   alt="University of Cologne" width="32" height="52" />
  <img id="shield" src="/images/shield.png"
     alt="Brown University" width="32" height="52" />
<h2>Wilson Sanskrit   Dictionary Scanned Images</h2>
</p>
<a id="top"></a>
<a href=#preface>PREFACE</a> <br />

<div id="words">

<p>
<?php
 $filename="wilfiles.txt";
 $file=fopen($filename,"r") or exit("Unable to open file $filename");
 $n = 0;
 $m = 9999; // make smaller for testing
 $pattern='/^wil-([0-9]+)-([a-zA-Z~]+)$/';
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
<a id="preface"><h2>Preface</h2></a> 
 (<a href=#top>back to top</a>)<br />
<p>
<?php
output_item($dir,$sfx,"wilson_Page_001","Title","");
output_item($dir,$sfx,"wilson_Page_002","Publisher","");
output_item($dir,$sfx,"wilson_Page_003","Dedication","");
output_item($dir,$sfx,"wilson_Page_004","Preface","");
output_item($dir,$sfx,"wilson_Page_005","Page vi","");
output_item($dir,$sfx,"wilson_Page_006","Page vii","");
?>
</p>
</div>

</body>
</html>
