<!DOCTYPE html>
<html>
<head>
<title>Cologne Scan</title>
</head>
<body>

<?php
$filename = $_GET['file'];
if (file_exists($filename)) {
 echo "<img src='$filename' width='1414' height='2000'/>\n";
}else {
 $chars = str_split($filename);
 echo "<br>file not found:<br>";
 foreach($chars as $c){
  echo "$c "; //the space is needed to thwart xss!
 }
}
?>
</body>
</html>
