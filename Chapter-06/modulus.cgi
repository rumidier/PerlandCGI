#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my $dividend = $formdata {'dividend'};
my $divisor = $formdata{'divisor'};

my $result = $dividend % $divisor;

print "Content-type: text/html\n\n";
print "<p>You entered $dividend for the dividend and $divisor for the
divided by $divisor is $result";
print "<p>The remainder of $dividend divided by $divisor is $result";
