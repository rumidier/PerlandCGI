#!/usr/bin/env perl

use strict;
use warnings;

&mime;
&header ("This is the page title");

print "This is more of that page wholly created by CGI and perl!";

&footer;

sub header {
    print "<html><head><title>";
    print "$_[0]";
    print "</title></head><body>";
}

sub footer {
    print "</body></html>";
}

sub mime {
    print "Content-type: text/html\n\n";
}
