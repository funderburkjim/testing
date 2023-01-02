#!/usr/bin/perl -w
#work/wilscan/getWord.pl
# 2008-09-05:  get data from wilscan table for a given key.
use CGI;
use CGI::Carp qw( fatalsToBrowser );
use DBI;
BEGIN {require "../../libutilcgi/SLPtransliterate.pm"; 
 SLPtransliterate->import qw(AS2SLP SLP2AS HK2SLP SLP2HK ITRANS2SLP SLP2ITRANS HKS2SLP SLP2HKS );
}

my $FILTER_DIR;
my @FILTERS = qw(SktRomanCSX SktRomanManjushreeCSX SktRomanUnicode
		 SktDevaUnicode SLP2HK SLP2ITRANS);

my $HEADER="<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"//www.w3.org/TR/html4/loose.dtd\">\n";



############################## MAIN ##############################

$| = 1;

my $cgi = new CGI;

my $keyin = $cgi->param('key');
$FILTER_DIR=$cgi->param('filterdir');
$FILTER_DIR="../../../docs/filter";
my $filter = $cgi->param('filter');
my $headerParm = $cgi->param('headerParm');
if ($headerParm) {
    if (($headerParm ne "YES") && ($headerParm ne "NO")){
	$headerParm="YES";
    }
}else {
    $headerParm="YES";
}
my $meta = "";
#$headerParm = "NO";
print $cgi->header(-type => 'text/html', -charset => 'UTF-8');
my $key;
$key = $keyin;

my $err = 0;

my  $dbh = DBI->connect ("DBI:mysql:sanskrit-lexicon:mysql.rrz.uni-koeln.de",
			 "sanskrit-lexicon","IwdsgmVns")
             || die "Could not connect to database: "
             . DBI-> errstr;
my $dbhout;
#my $info = process1_word($key);
my $info = make_json($key);

if ($info eq "") {
    $info = "[\"ERR\",\"$key\"]";
}
print $info;

if (0 == 1) {
print $cgi->end_html;
}
exit 0;
##
## end of main
##
sub make_json {
    # returns a json array.
    my ($key) = @_;
    my ($table,$sql);
    $table = "wilscan";
    $sql = "select * from `$table` where `key`=\"$key\"";
    my $dbhout = $dbh->prepare($sql);
    $dbhout->execute;
    my $ans="";
    
    my ($id,$data1);
    my ($temp);
    my $n = 0;
    while (($id,$data1)=$dbhout->fetchrow_array) {
	if ($n == 0) {
	    $ans="["; #begin json array
	    }
	$temp=make_json1($data1,$n,$id);
	if ($n != 0) {
	    $ans .= ","; #end previous elt of array with ,
	}
	$ans .= $temp;
	$n++;
    }
    if ($n != 0) {
	$ans .= "]"; #end json array
    }
    return $ans;
}
sub make_json1 {
    my ($x,$nmodels,$id1) = @_;
    my ($ans,$ans1);
    my ($n);
    if (!($x =~ /^(...)(..)<P[HAB]?>[.]<d>(....)-(..)-(...)-(...)-(...)<\/d>$/)) {
	return ("bad data");
    }
    my ($page,$par,$nc,$nl,$ncumtot1,$nltot,$pagetot);
    $page = $1;
    $par = $2;
    $nc = $3;
    $nl = $4;
    $ncumtot1=$5;
    $nltot = $6;
    $pagetot=$7;
    my $filename = page_2_file($page);
    # construct json object x:value
    $ans = "{" .
	"\"page\":\"$page\"," .
	"\"par\":\"$par\"," .
	"\"nc\":\"$nc\"," .
	"\"nl\":\"$nl\"," .
	"\"ncumtot1\":\"$ncumtot1\"," .
	"\"nltot\":\"$nltot\"," .
	"\"pagetot\":\"$pagetot\"," .
	"\"filename\":\"$filename\"" .
	"}";
    return $ans ;
}

sub process1_word {
    my $word = shift;
    my $info="";
    my $nfound1;
    $nfound1 = process_word($word,"wilscan");
    if ($nfound1 ne "") {
	$info = $nfound1;
    }
    return $info;
}
sub process_word {
    my ($key,$table) = @_;
    my $sql;
    $sql = "select * from `$table` where `key`=\"$key\"";
    my $dbhout = $dbh->prepare($sql);
    $dbhout->execute;
    my $ans="";
    my ($id,$data1);
    my ($temp);
    my $n = 0;
    while (($id,$data1)=$dbhout->fetchrow_array) {
	$temp=display_lgtab1($data1,$n,$id);
	if ($n < 5000) {
	    $ans .= $temp;
	}
	$n++;
    }
    return $ans;
}
sub display_lgtab1 {
    my ($x,$nmodels,$id1) = @_;
    my ($ans,$ans1);
    my ($n);
    if (!($x =~ /^(...)(..)<P[HAB]?>[.]<d>(....)-(..)-(...)-(...)-(...)<\/d>$/)) {
	return ("bad data");
    }
    my ($page,$par,$nc,$nl,$ncumtot1,$nltot,$pagetot);
    $page = $1;
    $par = $2;
    $nc = $3;
    $nl = $4;
    $ncumtot1=$5;
    $nltot = $6;
    $pagetot=$7;
    $ans = "<p>";
    $n = $nmodels+1;
    $ans .= "<span class='bold'>$n </span> ";
    $ans .= "$page,$par,$nc,$nl,$ncumtot1,$nltot,$pagetot";
    my $filename = page_2_file($page);
    $ans .= "  file = $filename";
    $ans .= "</p>\n";
    # get file name corresponding to $page
    return $ans ;
}
sub page_2_file {
    my $key = shift;
    my ($sql,$ans);
    my $table = "wilscanfiles";
    $sql = "select * from `$table` where `key`=\"$key\"";
    my $dbhout = $dbh->prepare($sql);
    $dbhout->execute;
    if (($id,$data1)=$dbhout->fetchrow_array) {
	$ans = $data1;
    }else {
	$ans = "No file for $key\n";
    }
    return $ans;
}
# Tell emacs that this is really a perl script
#Local Variables:
#Mode: perl
#End:
