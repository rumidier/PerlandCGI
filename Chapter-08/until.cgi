#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
my $start = $formdata{'start'};

print "Content-type: text/html\n\n";
print "<p>Starting countdown...";

until ($start <= 0) {
    print "$start....";
    --$start;
}
print "KABOOM";
