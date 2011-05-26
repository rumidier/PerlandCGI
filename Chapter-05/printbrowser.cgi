#!/usr/bin/env perl

use strict;
use warnings;

print "Content-type: text/html\n\n";

my $browser = $ENV{'HTTP_USER_AGENT'};
my $from = $ENV{'HTTP_REFERER'};

print "<p>You're browsing this page with $browser";
print "<p>And before this page, you were looking at $from";
