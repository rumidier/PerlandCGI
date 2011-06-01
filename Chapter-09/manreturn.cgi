#!/usr/bin/env perl

use strict;
use warnings;

&mime;
&header ("This is the page title");

print "This is more of that page wholly created by CGI and perl!";

my $capped_which = &cap (&which);
print "<p>You\'rebrowsing this page with $capped_which</p>";

&footer;

sub which {
	my $browser = $ENV{'HTTP_USER_AGENT'};

	if ($browser =~ /MSIE/) {
		$browser = "Explorer";
	} elsif ($browser =~ /Mozilla/) {
		$browser = "Netscape";
	} else {
		$browser = "something besides Netscape and Explorer";
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

sub cap {
    my $captext = $_[0];
    $captext =~tr/a-z/A-Z/;
    return $captext;
}
