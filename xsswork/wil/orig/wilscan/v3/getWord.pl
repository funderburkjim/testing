#!/usr/bin/perl -w
#work/wilscan/getWord.pl
# 2008-09-05:  get data from wilscan table for a given key.
use CGI;
use CGI::Carp qw( fatalsToBrowser );
use DBI;
use getfiles;
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
if (0 == 1) { # old code
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
}
print $cgi->header(-type => 'text/html', -charset => 'UTF-8');
my $key;
if (($keyin) && ($keyin =~ /^[0-9]+$/)) {
    $key = key_from_page($keyin);
    if (!($key)) {
	$key = $keyin;
    }
}else {
    $key = $keyin;
}
my $err = 0;

my  $dbh = DBI->connect ("DBI:mysql:sanskrit-lexicon:mysql.rrz.uni-koeln.de",
			 "sanskrit-lexicon","IwdsgmVns")
             || die "Could not connect to database: "
             . DBI-> errstr;
my $dbhout;
my $info="";
if ($key) {
    $info = make_json($key);
}
if ($info eq "") {
    $info = "[\"ERR\",\"$key\"]";
}
print $info;

exit 0;
##
## end of main
##
sub make_json {
    # returns a json array.
    my ($key) = @_;
    my ($table,$sql);
    $table = "wilscan";
#    $sql = "select * from `$table` where `key`=\"$key\"";
    $sql = "select * from `$table` where `key` LIKE \"$key%\"";
    my $dbhout = $dbh->prepare($sql);
    $dbhout->execute;
    my $ans="";
    
    my ($id,$data1);
    my ($temp,$page);
    my $n = 0;
    if (($id,$data1)=$dbhout->fetchrow_array) {
	$ans="["; #begin json array
	($temp,$page)=make_json1($data1,$n,$id,$key);
	$ans .= $temp;
	$n++;
    }
    if ($n != 0) {
	# get all the words on this page
	$sql = "select * from `$table` where `data` LIKE \"<p>$page%\"";
	$dbhout = $dbh->prepare($sql);
	$dbhout->execute;
	while (($id,$data1)=$dbhout->fetchrow_array) {
	    $temp=make_json2($data1,$n,$id);
	    $ans .= "," . $temp;
	    $n++;
	}
    }
    if ($n != 0) {
	$ans .= "]"; #end json array
    }
    return $ans;
}

sub make_json1 {
    my ($x,$nmodels,$id1,$key) = @_;
    my ($ans,$ans1);
    my ($n);
#   x = <p>98161</p><d>0-1-108-108-108</d>
    if (!($x =~ /^<p>(...)(..)<\/p><d>([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)<\/d>$/)) {
	return ("bad data");
    }
    my ($page,$par,$nh,$nl,$l1,$l2,$lt);
    $page = $1;
    $par = $2;
    $nh = $3;
    $nl = $4;
    $l1=$5;
    $l2 = $6;
    $lt=$7;
    my $tempdata = page_2_file($page); # debug method
    my @tempdata = split(/:/,$tempdata);
    my ($left,$top,$bot,$filename) = @tempdata;
    my ($fileprev,$filenext) = getprevnext($filename);
    # construct json object x:value
    $ans = "{" .
	"\"key\":\"$key\"," .
	"\"id\":\"$id1\"," .
	"\"page\":\"$page\"," .
	"\"par\":\"$par\"," .
	"\"nh\":\"$nh\"," .
	"\"nl\":\"$nl\"," .
	"\"l1\":\"$l1\"," .
	"\"l2\":\"$l2\"," .
	"\"lt\":\"$lt\"," .
	"\"filename\":\"$filename\"," .
	"\"fileprev\":\"$fileprev\"," .
	"\"filenext\":\"$filenext\"," .
	"\"left\":\"$left\"," .
	"\"top\":\"$top\"," .
	"\"bot\":\"$bot\"" .
	"}";
    return ($ans,$page) ;
}
sub make_json2 {
    my ($x,$nmodels,$id1) = @_;
    my ($ans,$ans1);
    my ($n);
#   x = <p>98161</p><d>0-1-108-108-108</d>
    if (!($x =~ /^<p>(...)(..)<\/p><d>([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)<\/d>$/)) {
	return ("bad data");
    }
    my ($page,$par,$nh,$nl,$l1,$l2,$lt);
    $page = $1;
    $par = $2;
    $nh = $3;
    $nl = $4;
    $l1=$5;
    $l2 = $6;
    $lt=$7;
    # construct json object x:value
    $ans = "{" .
	"\"id\":\"$id1\"," .
	"\"page\":\"$page\"," .
	"\"par\":\"$par\"," .
	"\"nh\":\"$nh\"," .
	"\"nl\":\"$nl\"," .
	"\"l1\":\"$l1\"," .
	"\"l2\":\"$l2\"," .
	"\"lt\":\"$lt\"" .
	"}";
    return $ans ;
}

sub page_2_sql {
    my $key = shift;
    my ($sql,$ans,$id,$data1);
    my $table = "wilscanfiles";
    $sql = "select * from `$table` where `key`=\"$key\"";
    my $dbhout = $dbh->prepare($sql);
    $dbhout->execute;
    if (($id,$data1)=$dbhout->fetchrow_array) {
	$ans = ($id,$data1);
    }else {
	$ans = ($key,"No file for $key\n");
    }
    return $ans;
}
sub page_2_file {
    my $page = shift;
    my ($x,$ans,$id,$data1,$xpage,$more);
    my $table = "../../../docs/scans/WILScan/mysql/wilscanfiles/wilscanfiles-rec.txt";
    open(my $in,"<",$table) or die "Can't open $table: $!\n";
    $ans = "No file for page $page\n";
    while (<$in>) {
	$x = $_;
	chomp($x);
	if (!($x =~ /wil-([0-9]+)-/)) {
	    return $ans;
	}
	$xpage = $1;
	if ($xpage == $page) {
	    $ans = $x;
	    close($in);
	    return $ans;
	}
    }
    close($in);
    return $ans;
}
sub key_from_page {
    my $page = shift;
    my ($x,$ans,$id,$data1,$xpage,$more,$temp);
    my $table = "../../../docs/scans/WILScan/mysql/wilscanfiles/wilscanfiles-rec.txt";
    open(my $in,"<",$table) or die "Can't open $table: $!\n";
    while (<$in>) {
	$x = $_;
	chomp($x);
	if (!($x =~ /wil-([0-9]+)-(.*?)$/)) {
	    return $ans;
	}
	$xpage = $1;
	$temp=$2;
#	print "'$page' '$xpage' temp=$temp\n";
	if ($xpage == $page) {
	    $ans = $temp;
	    close($in);
	    return $ans;
	}
    }
    close($in);
    return $ans;
}
sub getprevnext {
    my $filein = shift; # a partial filename, as in wilfiles.txt
    my $pathname = "/docs/scans/WILScan/WILScanjpg-deskew/$filein.jpg";
    my ($pathprev,$pathnext)=getfiles($pathname);
    my $fileprev = "";
    my $filenext = "";
    if ($pathprev =~ /^(.*?)\/([^\/.]*)[.](.*?)$/) {
	$fileprev = $2;
    }
    if ($pathnext =~ /^(.*?)\/([^\/.]*)[.](.*?)$/) {
	$filenext = $2;
    }
    return ($fileprev,$filenext);
}
sub make_json_version1 {
    # returns a json array.
    my ($key) = @_;
    my ($table,$sql);
    $table = "wilscan";
#    $sql = "select * from `$table` where `key`=\"$key\"";
    $sql = "select * from `$table` where `key` LIKE \"$key%\"";
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
	if ($n < 10) {
	    $temp=make_json1_version1($data1,$n,$id,$key);
	    if ($n != 0) {
		$ans .= ","; #end previous elt of array with ,
	    }
	    $ans .= $temp;
	}
	$n++;
    }
    if ($n != 0) {
	$ans .= "]"; #end json array
    }
    return $ans;
}
sub make_json1_version1 {
    my ($x,$nmodels,$id1,$key) = @_;
    my ($ans,$ans1);
    my ($n);
#   x = <p>98161</p><d>0-1-108-108-108</d>
    if (!($x =~ /^<p>(...)(..)<\/p><d>([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)<\/d>$/)) {
	return ("bad data");
    }
    my ($page,$par,$nh,$nl,$l1,$l2,$lt);
    $page = $1;
    $par = $2;
    $nh = $3;
    $nl = $4;
    $l1=$5;
    $l2 = $6;
    $lt=$7;
    my $tempdata = page_2_file($page); # debug method
    my @tempdata = split(/:/,$tempdata);
    my ($left,$top,$bot,$filename) = @tempdata;
    my ($fileprev,$filenext) = getprevnext($filename);
    # construct json object x:value
    $ans = "{" .
	"\"key\":\"$key\"," .
	"\"id\":\"$id1\"," .
	"\"page\":\"$page\"," .
	"\"par\":\"$par\"," .
	"\"nh\":\"$nh\"," .
	"\"nl\":\"$nl\"," .
	"\"l1\":\"$l1\"," .
	"\"l2\":\"$l2\"," .
	"\"lt\":\"$lt\"," .
	"\"filename\":\"$filename\"," .
	"\"fileprev\":\"$fileprev\"," .
	"\"filenext\":\"$filenext\"," .
	"\"left\":\"$left\"," .
	"\"top\":\"$top\"," .
	"\"bot\":\"$bot\"" .
	"}";
    return $ans ;
}
# Tell emacs that this is really a perl script
#Local Variables:
#Mode: perl
#End:
