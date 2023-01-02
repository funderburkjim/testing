<?php
function output_item ($filename,$word,$pagenum) {
    //$dir = '../pdfpages/';
    //$outfile=$dir . $filename . "." . $sfx;
    if ($word == 'SKIP') {return;}
    if (preg_match('|^[0-9]+|',$pagenum)) {
     echo "$pagenum &nbsp;&nbsp;";
    }
    #echo "<a href='../webtc/servepdf.php?page=$pagenum' target='output'>$word</a><br/>\n";
    echo "<a href='../web/webtc/servepdf.php?page=$pagenum' target='output'>$word</a><br/>\n";
    
 }
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "//www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="//www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <title>PGN Scan Input Form</title>
    <link rel="stylesheet" href="main.css">
  </head>
  <body>
<p>
  <!-- 10-09-2020
 <a href="//www.sanskrit-lexicon.uni-koeln.de/" target="_">
  <img id="unilogo" src="../images/cologne_univ_seal.gif"
   alt="University of Cologne"
   title="Cologne Sanskrit Lexicon"/> <!--width="32" height="52" 
 </a>
 -->
 <a href="//www.sanskrit-lexicon.uni-koeln.de/" target="_">
  <img id="unilogo" src="cologne_univ_seal.gif"
   alt="University of Cologne"
   title="Cologne Sanskrit Lexicon"/> <!--width="32" height="52" -->
 </a>
<h2>Names in the Gupta Inscriptions, Scanned Edition</h2>
<!--
</p>
<a id="top"></a>
<a href=#preface>PREFACE</a> <br />
<a href=#supplement>SUPPLEMENT</a> <br />
-->
<div id="words">
<p>
<?php
 //$filename="../webtc/pdffiles.txt";
 $filename = "pdfbookmarks.txt";
 $file=fopen($filename,"r") or exit("Unable to open file $filename");
 $n = 0;
 while(((!feof($file)))) {
   $n++;
   $line = fgets($file);
   $line = trim($line);
   list($pgid,$reffile,$title) = preg_split('|:|',$line);
   output_item($reffile,$title,$pgid);
  }

 fclose($file);
?>
</p>
</div>

<!--
<div>
<a id="supplement"><h2>Supplement: Additions and Corrections</h2></a> 
 (<a href=#top>back to top</a> )<br />
<?php

?>
</div>
-->
<!--
<div>
<a id="preface"><h2>Preface</h2></a> 
 (<a href=#top>back to top</a>)<br />
<p>
<?php
// output_item($dir,$sfx,"ae-vor-01","Title","");

?>
</p>
</div>
-->
</body>
</html>
