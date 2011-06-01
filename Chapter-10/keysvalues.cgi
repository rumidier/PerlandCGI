#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

print "Content-type: text/html\n\n";

print "<table><tr><th>Keys:</th><th>Values:</th></tr>";

foreach my $key (keys %formdata) {
    print "<tr><td>$key</td><td>$formdata{$key}</td></tr>";
}

print "</table>";
