package getfiles;
use Exporter ();
# work/wilscan/getfiles.pm
@ISA = qw(Exporter);
@EXPORT = qw(getfiles);
# expect parameter to be a filename with directory
# e.g. /docs/scans/WILScan/WILScanjpg-deskew/xyz.jpg
# returns a pair of files. 
# usage: my ($fileprev,$filenext)=getfiles($filename);
sub getfiles {
    my $matchin = shift;
    if (!($matchin)) {
	return (0,0);
    }
#    print "matchin = $matchin\n";
    if (!($matchin =~ /^(.*?)\/([^\/.]*)[.](.*?)$/)) {
	return (0,0);
    }
    my $dir = $1;
    my $match = $2;
    my $sfx = $3;
#    print "dir = $dir, match = $match, sfx = $sfx\n";
    my $filename="../../../docs/scans/WILScan/wilfiles.txt";
    my %MYFILE;
    if (not (open (MYFILE,$filename))) {
#	print "DBG: file not found\n";
	return (0,0);
    } 
    my $prev=0;
    my $next=0;
    my $line=<MYFILE>;
    my $more = 1;
    while (($line)&& ($more eq 1)) {
	chomp($line);
	if ($line eq $match) {
	    $next=<MYFILE>;
	    chomp($next);
	    $more = 0;
	    if (!($next)) {
		$next=0;
	    }
	} else {
	    $prev=$line;
	    $line=<MYFILE>;
	}
    }
    close(MYFILE);
    if ($more eq 1) {
	return (0,0);
    }
    $prev = "$dir/$prev.$sfx";
    $next = "$dir/$next.$sfx";
    return ($prev,$next);
}
# for some reason need the following
1;
# Tell emacs that this is really a perl script
#Local Variables:
#Mode: perl
#End:
