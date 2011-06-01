#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
my $food = $formdata{'food'};

print "Content-type: text/html\n\n";

unless ($food eq "spinach") {
    print "No spinach, no dessert!";
}
