#!/usr/bin/env perl 

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

print "Content-type: text/html\n\n";

foreach my $key (keys %formdata) {
    print "<p>The key is $key, the value is $formdata{$key}";
}
