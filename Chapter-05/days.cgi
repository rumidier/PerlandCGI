#!/usr/bin/env perl

use strict;
use warnings;

my @days = ("Monday", "Tyesday", "Wednesday", "Thursday",
         "Friday", "Saturday", "Sunday");

print "Content-type: text/html\n\n";
print "These arethe days of the week:";
print "<p>";
print "@days";
