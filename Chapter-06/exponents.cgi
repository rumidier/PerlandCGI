#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my $number = $formdata{'number'};
my $power = $formdata{'power'};

my $result = $number ** $power;

print "Content-type: text/html\n\n";
print "<p>You entered $number with an exponent of $power";
print "<p>$number raised to the $power power is $result.";
