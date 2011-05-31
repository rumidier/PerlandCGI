#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
my @classes = ("Latin 305", "Advaned Greek Grammar");
my $newclas = $formdata{'newclasses'};
my @newclasses = split(/,/, $newclas);

@classes = (@classes, @newclasses);

print "Content-type: text/html\n\n";

print "<h2>You added:</h2><ul>";

my $item;
foreach $item (@newclasses) {
    print "<li>$item</li>";
}
print "</ul>";
print "<h2>Your complete list is new:</h2><ul>";
foreach $item (@classes) {
    print "<li>$item</li>";
}
print "</ul>";
