#!/usr/bin/env perl

use strict;
use warnings;

my @days = qw ( Sunday Monday Tuesday Wendnesday Thursday Friday Saturday );

print "Content-type: text/html\n\n";
print "The first day of the week is $days[0]";
print "<p>The third day of the week is $days[2]";
