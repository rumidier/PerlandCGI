package Rumidier::SubParse::Subroutines;

use strict;
use warnings;

sub cap {
    my $captext = $_[0];
    $captext =~tr/a-z/A-Z/;

    return $captext;
}

sub which {
    my $browser = $ENV{'HTTP_USER_AGENT'};

    if ($browser =~ /MSIE/) {
        $browser = "Explorer";
    } elsif ($browser =~ /Mozilla/) {
        $browser = "Netscape";
    } else {
        $browser = "something besides Netscape
            and Explorer";
    }
}

sub header {
    print "<html><head><title>";
    print "$_";
    print "</title></head><body>";
}

sub footer {
    print "</body></html>";
}
sub mime {
    print "Content-type: text/html\n\n";
}

1;
