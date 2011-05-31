#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my @classes = ("Latin 305", "Advanced Greek Grammar", "Applied Linguistics",
        "Virgil and the Iliad");
my $removed = shift(@classes);

print "Content-type: text/html\n\n";

print "<h2>You removed $removed. your complete list is now:</h2><ul>";

foreach my $item (@classes) {
    print "<li>$item</li>";
}

print "</ul>";
