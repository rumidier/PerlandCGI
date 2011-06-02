#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
print "Content-type: text/html\n\n";

my $zip = $formdata{'zip'};

if ($zip =~ /[^0-9\-]/) {
    print "Your zipcode should only contain the numbers or the dash. Try
        again.";
} else {
    print "You entered $zip for your zipcode";
}
