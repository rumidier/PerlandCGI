#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

print "Content-type: text/html\n\n";

my $phrase = $formdata{'phrase'};
$phrase =~ s/damn/hoot/g;

print "<p>Your more proper sentence is</p><b>$phrase</b>";
