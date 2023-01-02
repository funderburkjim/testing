<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "//www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">

<html xmlns="//www.w3.org/1999/xhtml"  lang="en" xml:lang="en">
  <head>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=iso-8859-1">
    <title>PW Scan
    <?php
     $vol = $_GET['vol'];
     if (!in_array($vol,array('1','2','3','4','5','6','7'))) {
      $vol = '1';
     }
     echo " Vol $vol";
    ?>
    </title>
  </head>

<frameset cols="200,*">
<?php
 // 11-28-2022 Only jpg and png are accepted. jpg is default.
 $sfx = 'jpg';
 if (isset($_GET['sfx'])) {
  $sfx = $_GET['sfx'];
  if (!in_array($sfx,array('jpg','png'))) {
   $sfx = 'jpg';
  }
 }
 $vol = '1';
 if (isset($_GET['vol'])) {
  $vol = $_GET['vol'];
 }
 if (!in_array($vol,array('1','2','3','4','5','6','7'))) {
  $vol = '1';
 }
 echo "<frame src=\"form.php?sfx=$sfx&vol=$vol\" name=\"navigate\">\n";
?>
<frame src="empty.html" name="output">
</frameset>
</html>
