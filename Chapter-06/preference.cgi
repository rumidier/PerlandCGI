#!/usr/bin/env perl

use strict;
use warnings;

my $div = 40 / 5 + 3;
my $parens = 40 / (5 + 3);
my $subadd = 9 - 3 + 5;
my $parens_subadd = 9 - (3 + 5);

print "Content-type: text/html\n\n";
print "div is $div, parens is $parens, subadd is $subadd and
parens_subadd is $parens_subadd :"

