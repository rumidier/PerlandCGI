#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
my $food = $formdata{'food'};
print "Content-type: text/html\n\n";

if ($food eq "spinach") {
    print "You ate spinach, so you get dessert!";
} elsif ($food eq "broccoli") {
    print "Broccoli's OK. Maybe you'll get dessert.";
} else {
    print "No spinach, no dessert!";
}

