#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my @numbers = split(/,/, $formdata{'number'});
print "Content-type: text/html\n\n";
print "The numbers you entered were:";

my $number;
foreach $number (@numbers) {
    print "<li>$number</li>";
}

foreach $number(@numbers) {
    $number = sqrt($number);
}

print "<p>The square roots of those numbers are: ";
foreach $number(@numbers) {
    print "<li>$number</li>";
}
