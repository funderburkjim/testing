<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "//www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">

<html xmlns="//www.w3.org/1999/xhtml"  lang="en" xml:lang="en">
  <head>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=iso-8859-1">
    <title>MW Scan</title>
  </head>

<frameset cols="200,*">
<?php
 $sfx = $_GET['sfx'];
 echo "<frame src=\"form.php?sfx=$sfx\" name=\"navigate\">\n";
?>
<frame src="empty.html" name="output">
</frameset>
</html>
