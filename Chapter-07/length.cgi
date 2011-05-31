#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my $class = $formdata{'class'};
my @classes = split(/,/, $class);
my $amount = @classes;

print "Content-type: text/html\n\n";

print "<h2>You chose $amount classes.  Thet are:</h2><ul>";

foreach my $item (@classes) {
    print "<li>$item</li>";
}

print "</ul>";
