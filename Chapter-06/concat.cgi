#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my $first = $formdata{'first_name'};
my $married = $formdata{'fiance_last'};

my $fullname = $first." ".$married;

print "Content-type: text/html\n\n";
print "Congratulations! Your married name would be $fullname.";
