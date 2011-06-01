#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my @name = @formdata{'first', 'last'};

print "Content-type: text/html\n\n";
print "You entered a first name of <b>@name</b>";
