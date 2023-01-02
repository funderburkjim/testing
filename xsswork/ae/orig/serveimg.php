<?php
// this perl code could be converted to php to display jpg images.
#!/usr/bin/perl -w
# 10/11/2006   01-04-2006
use CGI;
use CGI::Carp qw( fatalsToBrowser );
$| = 1;

my $cgi = new CGI;
my $filename = $cgi->param('file') ;
my $width = $cgi->param('width');
my $height = $cgi->param('height');
print $cgi->header(-type => 'text/html', -charset => 'UTF-8');
my $HEADER='<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "//www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">';
$HEADER .= 
  '<html xmlns="//www.w3.org/1999/xhtml" lang="en" xml:lang="en">';
$HEADER .= '<head>';
$HEADER .= '<title>Cologne Scan</title>';
 
$HEADER .= "</head><body>\n";
print $HEADER ;
if (!$width) {$width=0;}
if (!$height) {$height=0;}
if ((0 < $width) and (0 < $height)) {
#    my $size = "width=\"$width" . px . "\" height=\"$height" . px . "\"";
    my $size = "width=\"$width" . "px" . "\" height=\"$height" . "px" . "\"";
    print "<img src=\"$filename\" $size />";
}else {
    print "<img src=\"$filename\" />";
}
print $cgi->end_html;
?>
