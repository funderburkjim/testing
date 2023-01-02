#!/usr/bin/perl -w
#work/stcscan/getWord.pl
# 2008-11-24:  get data from stcscan table for a given key.
# 2020-10-20:  Revise to NOT use filters. Require user to use HK
use CGI;
use CGI::Carp qw( fatalsToBrowser );
use DBI;
use getfiles;
# comment out 10-9-2020
#BEGIN {require "../../libutilcgi/SLPtransliterate.pm"; 
 #SLPtransliterate->import qw(AS2SLP SLP2AS HK2SLP SLP2HK ITRANS2SLP SLP2ITRANS HKS2SLP SLP2HKS );
#}

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
#my $filter = $cgi->param('filter');   # comment out 10-9-2020
#my $transLit= $cgi->param('transLit');   # comment out 10-9-2020
if (!($transLit)) {
    $transLit="HK";
}

print $cgi->header(-type => 'text/html', -charset => 'UTF-8');
my $key;
#print "$keyin, $key\n";
my $pagein;
if (($keyin) && ($keyin =~ /^[0-9]+$/)) {
    $key = key_from_page($keyin);
    $pagein = $keyin; # number
    if (!($key)) {
	$key = $keyin;
    }
}else {
    $key = $keyin;
#    $key = translate_string2HK($transLit,$keyin); # comment out
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
# use filter to output the result
if ($filter) {
    open FILTER, "| $FILTER_DIR/$filter";
    print FILTER $info;
    close FILTER;
} else {
    $info =~ s/<\/?SA>//g;
    print $info;
}

exit 0;
##
## end of main
##
sub make_json {
    # returns a json array.
    my ($key) = @_;
    my ($table,$sql);
    $table = "stcscan";
#    $sql = "select * from `$table` where `key`=\"$key\"";
    $sql = "select * from `$table` where `key` LIKE \"$key%\"";
    my $dbhout = $dbh->prepare($sql);
    $dbhout->execute;
    my $ans="";
    
    my ($id,$data1,$id1);
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
	my $tempdata = page_2_file($page); # debug method
	my @tempdata = split(/:/,$tempdata);
	my ($left,$top,$bot,$filename) = @tempdata;
	$sql = "select * from `$table` where `data` LIKE \"$page%\"";
	$dbhout = $dbh->prepare($sql);
	$dbhout->execute;
	while (($id1,$data1)=$dbhout->fetchrow_array) {
	    $temp=make_json2($data1,$n,$id1,$left,$top,$bot,);
	    $ans .= "," . $temp;
	    $n++;
	}
    }
    if ($n != 0) {
	$ans .= "]"; #end json array
    }
    if (($n == 0)&&$pagein) {
	# this situation happens rarely. Example pagein = 113.
	my $tempdata = page_2_file($pagein); # debug method 
	my @tempdata = split(/:/,$tempdata);
	my ($left,$top,$bot,$filename) = @tempdata;
	my ($fileprev,$filenext) = getprevnext($filename);
	# correction of Feb 18, 2011
	if (!$left) {$left=0;}
	if (!$top) {$top=0;}
	if (!$bot) {$bot=0;}
	if (!$filename) {$filename=0;}
	$ans = "["; # begin json array
	my $ans1 = "{" .
	"\"page\":\"$pagein\"," .  # note use of $pagein
	"\"filename\":\"$filename\"," .
	"\"fileprev\":\"$fileprev\"," .
	"\"filenext\":\"$filenext\"," .
	"\"left\":\"$left\"," .
	"\"top\":\"$top\"," .
	"\"bot\":\"$bot\"" .
	"}";
	$ans .= $ans1;
	$ans .= "]"; #end json array
   }
    return $ans;
}

sub make_json1 {
    my ($x,$nmodels,$id1,$key) = @_;
    my ($ans,$ans1);
    my ($n);
# x =  page-col-nh1-npar-j1-i1-j2-i2
# nh1 = # of preceding <H> in column
# npar = current paragraph number (in column)
# j1 = # of preceding <P>{%..%} sub headword lines in column (for headword)
# i1 = # of preceding continuation lines (for headword)
# j2 = # of preceding <>{%..%} for last line of paragraph
# i2 = # of preceding continuation lines  for last line of paragraph.
# a       001-1-1-1-0-0-0-0

    my ($page,$col,$nh,$par,$j1,$i1,$j2,$i2) = split(/-/,$x);
    $tempdata = page_2_file($page); # debug method
    #$tempdata = page_2_sql($page); # this doesn't work for some reason
    my @tempdata = split(/:/,$tempdata);
    my ($left,$top,$bot,$filename) = @tempdata;
    my ($fileprev,$filenext) = getprevnext($filename);
    my $id2 = $id1; #HK2SLP($id1); 10-9-2020
    # construct json object x:value
    $ans = "{" .
	"\"key\":\"$key\"," .
	"\"id\":\"$id1\"," .
	"\"iddisp\":\"<SA>$id2</SA>\"," .  # prepare for transformation
	"\"page\":\"$page\"," .
	"\"col\":\"$col\"," .
	"\"par\":\"$par\"," .

	"\"nh\":\"$nh\"," .
	"\"j1\":\"$j1\"," .
	"\"i1\":\"$i1\"," .
	"\"j2\":\"$j2\"," .
	"\"i2\":\"$i2\"," .

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
    my ($x,$nmodels,$id1,$left,$top,$bot,) = @_;
    my ($ans,$ans1);
    my ($n);
    my ($page,$col,$nh,$par,$j1,$i1,$j2,$i2) = split(/-/,$x);
   # id1 is in HK format
    my $id2 = $id1;  # HK2SLP($id1); 10-9-2020
    # construct json object x:value
    $ans = "{" .
	"\"id\":\"$id1\"," .
	"\"iddisp\":\"<SA>$id2</SA>\"," .  # prepare for transformation
	"\"page\":\"$page\"," .
	"\"col\":\"$col\"," .
	"\"par\":\"$par\"," .

	"\"nh\":\"$nh\"," .
	"\"j1\":\"$j1\"," .
	"\"i1\":\"$i1\"," .
	"\"j2\":\"$j2\"," .
	"\"i2\":\"$i2\"," .

	"\"left\":\"$left\"," .
	"\"top\":\"$top\"," .
	"\"bot\":\"$bot\"" .
	"}";
    return $ans ;
}

sub page_2_sql { # this doesn't work properly
    my $key = shift;
    my ($sql,@ans,$id,$data1);
    my $table = "stcscanfiles";
    $sql = "select * from `$table` where `key`=\"$key\"";
    my $dbhout = $dbh->prepare($sql);
    $dbhout->execute;
    if (($id,$data1)=$dbhout->fetchrow_array) {
	@ans = ($id,$data1);
    }else {
	@ans = ($key,"No file for $key\n");
    }
    return @ans;
}
sub page_2_file {
    my $page = shift;
    my ($x,$ans,$id,$data1,$xpage,$more);
    my $table = "../../../docs/scans/STCScan/mysql/stcscanfiles/stcscanfiles-rec.txt";
    open(my $in,"<",$table) or die "Can't open $table: $!\n";
    $ans = "No file for page $page\n";
    while (<$in>) {
	$x = $_;
	chomp($x);
	if (!($x =~ /stchou-([0-9]+)-/)) {
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
    my $table = "../../../docs/scans/STCScan/mysql/stcscanfiles/stcscanfiles-rec.txt";
    open(my $in,"<",$table) or die "Can't open $table: $!\n";
    while (<$in>) {
	$x = $_;
	chomp($x);
	if (!($x =~ /stchou-([0-9]+)-(.*?)$/)) {
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
    my $pathname = "/docs/scans/STCScan/STCScanjpg/$filein.jpg";
    my ($pathprev,$pathnext)=getfiles($pathname);
#    print "DBG: $pathname\n  $pathprev\n  $pathnext\n";
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
sub translate_string2HK {
    my ($transLit,$x) = @_;
    if ($transLit =~  /^SLP/) {
	$x = SLP2HK($x);
    }elsif ($transLit =~ /ITRANS/) {
	$x = ITRANS2HK($x);
    }
    $x;
}

# Tell emacs that this is really a perl script
#Local Variables:
#Mode: perl
#End:
