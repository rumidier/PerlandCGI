#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my @values = values(%formdata);

print "Content-type: text/html\n\n";
print "<h2>Values:</h2><ul>";

foreach my $value (@values) {
    print "<li>$value</li>";
}
print "</ul>";
