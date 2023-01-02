<?php
 $sfx = $_GET['sfx'];
 // for pdf, directory is relative to this 'xxview' directory;
 // for images, directory use relative to that of ../serveimg.pl
 if ($sfx == "pdf"){
  $dir="/scans/STCScan/STCScan" . $sfx . "/";
 }
 else {
  $dir="/scans/STCScan/STCScan" . $sfx . "/";
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
    <title>STC Scan Input Form</title>
    <link rel="stylesheet" href="/css/main.css">
<p>
  <img id="unilogo" src="/images/unilogo.gif"
   alt="University of Cologne" width="32" height="52" />
  <img id="shield" src="/images/shield.png"
     alt="Brown University" width="32" height="52" />
<h2>Stchoupak Sanskrit-French Dictionary Scanned Images</h2>
</p>
<a id="top"></a>
<a href=#preface>PREFACE</a> <br />

<div id="words">

<p>
<?php
 $filename="stcfiles.txt";
 $file=fopen($filename,"r") or exit("Unable to open file $filename");
 $n = 0;
 $m = 9999; // make smaller for testing
 $pattern='/^stchou-([0-9]+)-(.*?)$/';
 while(((!feof($file)) && ($n < $m))) {
   $n++;
   $line = fgets($file);
   if (preg_match($pattern,$line,$matches)) {
    $reffile=$matches[0];
    $pagenum= $matches[1];
    $word = $matches[2];
//    $word= "Page " . $pagenum;
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
output_item($dir,$sfx,"stchou-vor0001","Title","");
output_item($dir,$sfx,"stchou-vor0005","Preface i","");
output_item($dir,$sfx,"stchou-vor0007","Preface ii","");
output_item($dir,$sfx,"stchou-vor0008","Preface iii","");
output_item($dir,$sfx,"stchou-vor0009","Page iv","");
?>
</p>
</div>

</body>
</html>
