#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
print "Content-type: text/html\n\n";

my $name = $formdata{'name'};
my @prey = split (/,/, $formdata{'prey'});

foreach my $creature (@prey) {
    print "<p>$name likes to eat $creature.</p>";
}
