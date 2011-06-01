#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

print "Content-type: text/html\n\n";

if (exists $formdata{'sales'}) {
    print "You came to this script from the Sales page";
} elsif (exists $formdata{'first'}) {
    print "You came to this script from the general info page";
} else {
    print "I don't know how you accessed this script";
}
