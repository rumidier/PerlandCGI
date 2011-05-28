#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my $total = $formdata{'donation'};
my $times = $formdata{'times'};
my $premium = $formdata{'premium'};

my $average = $total/$times;
my $tax_deduction = $total - $premium;

print "Content-type: text/html\n\n";
print "<p>You donated $total dollars last year. Thank you.";
print "<p>Since you donated $times times, that works out to an average of
       $average dollars per donation.";
print "<p>Since your premium was worth $premium dollars, you can only take a
tax deduction of $tax_deduction dollars.";
