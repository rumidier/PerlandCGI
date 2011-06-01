#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

print "Content-type: text/html\n\n";

while (my ($key, $value) = each (%formdata)) {
    print "<p>The key is $key and the value is $value</p>";
}
