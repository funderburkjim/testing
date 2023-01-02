<?php
 function output_option ($value,$display,$initvalue) {
  echo "  <option value='$value'";
  if ($initvalue == $value) {
   echo " selected='selected'";
  }else if ($value == "HK") {
   echo " selected='selected'";
  }
  echo ">$display</option>\n";
}
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "//www.w3.org/TR/html4/loose.dtd">
<html>
 <head>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">
    <title>Stchoupak</title>
    <!-- <link rel="stylesheet" href="/css/main.css"> 10-09-2020 -->
    <link rel="stylesheet" href="main_main.css">
    <link rel="stylesheet" href="main.css" type="text/css">
  
  <!-- <script type="text/javascript" src="/mwquery/ajax.js"> </script> 
    changed 10-09-2020 (ejf)
  -->
  <script type="text/javascript" src="ajax.js"> </script>
  <script type="text/javascript" src="main.js"> </script>
 </head>
 <body onLoad='loadFcn();'>
 <div id="titlediv">
 <table><tr>
  <td> <img id="unilogo" src="/images/unilogo.gif"
   alt="University of Cologne" width="60" height="60" />
  </td>
 <td>Dictionnaire sanscrit-français Stchoupak</td>
 </tr>
<tr>
<td colspan="2">
<a href="help_fr.html"><span style="color:maroon">Aide</span></a>
&nbsp;&nbsp;
 <a href="corrections.html"><span style="color:maroon">Corrections</span></a>
&nbsp;&nbsp;
 <a href="//www.sanskrit-lexicon.uni-koeln.de/index.html"><span style="color:maroon">Accueil</span></a>

</td>
<!--
<td>
 <a href="help_fr.html"><span style="color:maroon">Aide</span></a>
</td>
<td>
 <a href="corrections.html"><span style="color:maroon">Corrections</span></a>
</td>

<td>
 <a href="//www.sanskrit-lexicon.uni-koeln.de/index.html"><span style="color:maroon">Accueil</span></a>
</td>
-->
 </tr> </table>
</span>
 </div>
<div id="citationdiv">
<div id="keydiv">
<?php
 $init=$_GET['key'];
 echo '<input type="text" name="key" size="18" id="key" ';
 if (!($init)) {
  $init = "";
 }
 echo "value=\"$init\"";
 echo ' onkeypress="return queryInputChar(event);" />' . "\n";
?>
</div>
<div id="translitdiv">
<select name="transLit" id="transLit" id="translitdiv">
<?php
 $init=$_GET['transLit'];
 output_option("HK","HK",$init);
 # 10-09-2020
 #output_option("SLP","SLP",$init);
 #output_option("ITRANS","ITR",$init);

?>
 </select>
 &nbsp; <select name="filter" id="filter">
<?php
 $init=$_GET['filter'];
 if ($init == "SLP") {
  $init="SLP2SLP";
 }else if ($init == "HK") {
  $init = "HK2SLP";
 }else if ($init == "ITR") {
  $init = "ITRANS2SLP";
 }else {
  $init = "HK";
 }
 $init = "HK"; # 10-09-2020
 #output_option("SktDevaUnicode","DevU",$init);
 output_option("SLP2HK","HK",$init);
 #output_option("","SLP",$init);
 #output_option("SLP2ITRANS","ITR",$init);
 #output_option("SktRomanUnicode","RomU",$init);
 #output_option("SktRomanCSX","CSX",$init);
 #output_option("SktRomanManjushreeCSX","MCSX",$init);
?>
    </select>
<br/>
<select name='autoscroll' id='autoscroll'>
<?php
 output_option('scroll','scroll','scroll');
 output_option('npscroll','noscroll','noscroll');
?>
</select>
 <input type="hidden" name="filterdir" value="/docs/filter" id="filterdir">

  
</div>

<div id="botleftdiv">
<p style="color:red">WARNING: This program not fully functional <br/>(10-09-2020)</p>
</div>
</div>
<div id="rightpane">
  <div id="hilitediv">
  </div>
</div>
<div id="rightpanebk">
</div>
</body>
</html>
