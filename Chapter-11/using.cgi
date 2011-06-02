#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
print "Content-type: text/html\n\n";

my $address = $formdata{'address'};

if ($address =~ /(\d{5}(-\d{4})?)/) {
    print "I found a zip code of $2. Is that correct?";
} else {
    print "No zip code was found.";
}
