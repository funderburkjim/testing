#!/usr/bin/perl -w
# 10/11/2006   01-04-2006
#for wilscan 11-14-2008
use CGI;
use CGI::Carp qw( fatalsToBrowser );
use getfiles;
$| = 1;

my $cgi = new CGI;
my $filename = $cgi->param('file') ;
# an onload attribute for <img>, may be absent
my $scroll =  $cgi->param('scroll') ;
if (!($scroll)) {
    $scroll="";
}else {
    $scroll = 'onload="scroll_div(\'rightpane\'' + $scroll + ')"';
}
$scroll="";
my ($fileprev,$filenext)=getfiles($filename);
print $cgi->header(-type => 'text/html', -charset => 'UTF-8');
my $HEADER='<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "//www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">';
$HEADER .= 
  '<html xmlns="//www.w3.org/1999/xhtml" lang="en" xml:lang="en">';
$HEADER .= '<head>';
$HEADER .= '<title>Cologne Scan</title>';
 
$HEADER .= "<link rel='stylesheet' type='text/css' href=\"/css/monier_serveimg.css\" />";
$HEADER .= "</head><body>\n";
# print $HEADER ;
print "<img src=\"$filename\" $scroll ></img>";
print "<div id='pagenav'>\n";
genDisplayFile("&lt;",$fileprev);
genDisplayFile("&gt;",$filenext);
print "</div>\n";
print $cgi->end_html;
exit;

sub genDisplayFile {
    my ($text,$file) = @_;
    my $href = "/cgi-bin/work/wilscan/serveimg.pl?file=$file";
    my $a = "<a href='$href' class='nppage'><span class='nppage1'>$text</span>&nbsp;</a>";
    print "$a\n";
}
