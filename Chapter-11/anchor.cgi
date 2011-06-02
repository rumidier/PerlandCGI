#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
print "Content-type: text/html\n\n";
my $phone = $formdata{'phone'};

if ($phone =~ /^(\(\d\d\d\))? ?\d\d\d-\d\d\d\d$/) {
    print "You entered a phone number of $phone.";
} else {
    print "Please enter the phone number in the form <p>(123) 456-7890</p>";
}
