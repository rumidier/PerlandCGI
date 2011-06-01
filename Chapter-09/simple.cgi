#!/usr/bin/env perl

use strict;
use warnings;

mime();
print "<html><head><title>A new page</title></head><body>";
print "This page wholly created with CGI and Perl!";
print "</body></html>";

sub mime {
	print "Content-type: text/html\n\n";
}
