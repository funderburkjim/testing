<?php
// 11-28-2022. Modify to avoid xss vulnerability.
// sfx must be jpg
 // Require $vol be 1,2,3,4,5,6, or 7
 $sfx = 'jpg'; // default.
 if (isset($_GET['sfx'])) {
  $sfx = $_GET['sfx'];
  if (!in_array($sfx,array('jpg'))) {
   $sfx = 'jpg';
  }
 }
 $sfx = $_GET['sfx'];
 $dir="/scans/PWScan/PWScan" . $sfx . "/";
 $vol = $_GET['vol'];
 if (!in_array($vol,array('1','2','3','4','5','6','7'))) {
  $vol = '1';
 }

function output_item ($dir,$sfx,$filename,$word,$pagenum) {
    $outfile=$dir . $filename . "." . $sfx;
    echo "$pagenum";
    echo "&nbsp;&nbsp;";
    echo "<a href='serveimg.php?file=$outfile'";

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
    <title>PW Scan Input Form</title>
    <link rel="stylesheet" href="/css/main.css">
<p>
  <img id="unilogo" src="/images/unilogo.gif"
   alt="University of Cologne" width="32" height="52" />
  <img id="shield" src="/images/shield.png"
     alt="Brown University" width="32" height="52" />
<h2>Boehtlingk and Roth Greater Sanskrit  Dictionary Scanned Images
<br />
 <?php
 echo "Vol $vol" 
 ?>
</h2>

</p>
<a id="top"></a>
<a href=#preface>PREFACE</a> <br />
<a href=#notes>NOTES</a> <br />

<div id="words">

<p>
<?php
 $filename="pwfiles.txt";
 $file=fopen($filename,"r") or exit("Unable to open file $filename");
 $n = 0;
 $m = 9999; // make smaller for testing
 $pattern="/^pw" . $vol . "-([0-9]+)--([a-zA-Z~']+)$/";
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
 $filename="pwfiles.txt";
 $file=fopen($filename,"r") or exit("Unable to open file $filename");
 $n = 0;
 $m = 9999; // make smaller for testing
 $pattern="/^pw" . $vol . "-([0-9]+)-([0-9]+)$/";
 while(((!feof($file)) && ($n < $m))) {
   $n++;
   $line = fgets($file);
   if (preg_match($pattern,$line,$matches)) {
    $reffile=$matches[0];
    $word = $matches[2]; // page #
    $pagenum= $matches[1]; // always 000
    output_item($dir,$sfx,$reffile,"p. $word","");
   }
  }
 fclose($file);
?>
</p>
</div>

<div>
<a id="notes"><h2>Notes</h2></a> 
 (<a href=#top>back to top</a>)<br />
<p>
<?php
 $filename="pwfiles.txt";
 $file=fopen($filename,"r") or exit("Unable to open file $filename");
 $n = 0;
 $m = 9999; // make smaller for testing
 $pattern="/^pw" . $vol . "-([0-9]+)N$/";
 while(((!feof($file)) && ($n < $m))) {
   $n++;
   $line = fgets($file);
   if (preg_match($pattern,$line,$matches)) {
    $reffile=$matches[0];
//    $word = $matches[2]; 
    $pagenum= $matches[1]; // page #
    output_item($dir,$sfx,$reffile,"p. $pagenum","");
   }
  }
 fclose($file);
?>
</p>
</div>

</body>
</html>
