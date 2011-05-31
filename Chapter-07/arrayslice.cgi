#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my @days = qw{Sunday Monday Tuesday Wednesday Thursday Friday Saturday};

my @choice = split(/,/, $formdata{'choice'});

print "Content-type: text/html\n\n";
print "You chose @days[@choice]";
