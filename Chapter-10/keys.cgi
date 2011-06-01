#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my @keys = keys (%formdata);

print "Content-type: text/html\n\n";
print "<h2>Values:</h2><ul>";

foreach my $key (@keys) {
    print "<li>$key</li>";
}
print "</ul>";
