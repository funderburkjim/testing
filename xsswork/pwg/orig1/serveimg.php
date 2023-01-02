<!DOCTYPE html>
<html>
<head>
<title>Cologne Scan</title>
</head>
<body>


<?php
// this perl code could be converted to php to display jpg images.
$filename = $_GET['file'];
echo "<img src='$filename' width='1414' height='2000'/>\n";

/* In case we want to play with dimensions
my $width = $cgi->param('width');
my $height = $cgi->param('height');

if (!$width) {$width=0;}
if (!$height) {$height=0;}
if ((0 < $width) and (0 < $height)) {
#    my $size = "width=\"$width" . px . "\" height=\"$height" . px . "\"";
    my $size = "width=\"$width" . "px" . "\" height=\"$height" . "px" . "\"";
    print "<img src=\"$filename\" $size />";
}else {
    echo "<img src=\"$filename\" />";
}
*/

?>
</body>
</html>
