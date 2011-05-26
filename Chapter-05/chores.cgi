#!/usr/bin/env perl

use strict;
use warnings;

my %chores = (
        "Monday", "vacuum",
        "Wednesday", "mop",
        "Friday", "wash windows"
        );
print "Content-type: text/html\n\n";
foreach my $day (keys (%chores)) {
    print "<p>On $day, we have to $chores{$day}\n";
}
