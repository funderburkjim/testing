<?php
function output_item ($filename,$word,$pagenum) {
//    $outfile=$dir . $filename . "." . $sfx;
    $sfx = "png";
    $dir="/scans/SCHScan/SCHScan" . $sfx . "/";
    $outfile = $dir . $filename;
    if ($pagenum != '') {
     echo "$pagenum";
     echo "&nbsp;&nbsp;";
    }
    // page size = 2568px × 3780px
//    $width = "700"; $height = "1030";
//  $width = "900"; $height = "1325";
    $width = "1284"; $height = "1890";
    echo "<a href=\"/cgi-bin/serveimg.pl?file=$outfile&width=$width&height=$height\"";
    echo " target=\"output\">$word</a>";
    echo "<br />";
    echo "\n";
 }
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <title>Schmidt Scan Input Form</title>
    <link rel="stylesheet" href="/css/main.css">
<p>
  <img id="unilogo" src="/images/unilogo.gif"
   alt="University of Cologne" width="32" height="52" />
<h2>Schmidt Sanskrit Dictionary Scanned Images
<br />
</h2>

</p>
<a id="top"></a>
<a href=#preface>PREFACE</a> <br />

<div id="words">

<p>
<?php
 $filename="schfiles.txt";
 $file=fopen($filename,"r") or exit("Unable to open file $filename");
 $n = 0;
 $m = 9999; // make smaller for testing
 $pattern="/^([^ ]+) sch-([0-9]+)[.]png$/";
 while(((!feof($file)) && ($n < $m))) {
   $n++;
   $line = fgets($file);
   if (preg_match($pattern,$line,$matches)) {
    $word = $matches[1];
    $pagenum= $matches[2];
    $reffile="sch-$pagenum.png";
    output_item($reffile,$word,$pagenum);
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
 $filename="schfiles.txt";
 $file=fopen($filename,"r") or exit("Unable to open file $filename");
 $n = 0;
 $m = 9999; // make smaller for testing
 $pattern="/^sch-tit-([0-9]+)[.]png$/";
 $pattern="/^([^ ]+) sch-tit-([0-9]+)[.]png$/";
 while(((!feof($file)) && ($n < $m))) {
   $n++;
   $line = fgets($file);
   if (preg_match($pattern,$line,$matches)) {
    $word = $matches[1];
    $pagenum= $matches[2];
    $reffile="sch-tit-$pagenum.png";
    output_item($reffile,$word,"");
   }
  }
 fclose($file);
?>
</p>
</div>


</body>
</html>
