#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
my @classes = ("Latin 305", "Advanced Greek Grammar");
my $newclass = $formdata{'newclass'};

unshift(@classes, $newclass);

print "Content-type: text/html\n\n";

print "<h2>You added $newclass. Your Complete list is now:</h2><ul>";

foreach my $item (@classes) {
    print "<li>$item</li>";
}

print "</ul>";
