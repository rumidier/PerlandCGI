#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my $spouse = $formdata{'spouse'};
my @qualifications = split(/,/, $spouse);

print "Content-type: text/html\n\n";

print "<font size=+1><ul><b>You chose:</b>";

foreach my $item (@qualifications) {
    print "<li>$item</li>";
}

print "</ul></font>";
