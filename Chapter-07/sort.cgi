#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my $class = $formdata{'class'};
my @classes = split(/,/, $class);

print "Content-type: text/html\n\n";
print "<h2>You chose:</h2><ul>";

@classes = sort (@classes);

foreach my $item (@classes) {
    print "<li>$item</li>";
}
