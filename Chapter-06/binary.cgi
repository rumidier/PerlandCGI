#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my $counter = $formdata{'counter'};
$counter += 1;

print "Content-type: text/html\n\n";
print "<font size = +2> If you add one to your number, the result is
<b>$counter</b>";

$counter += 5;
print "<p>if you add 5 to that, the result is <b>$counter</b></font>";
