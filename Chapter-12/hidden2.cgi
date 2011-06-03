#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
print "Content-type: text/html\n\n";
print "<html><head><title>Using Hidden Fields</title></head><body>";

print "The item ordered by $formdata{'name'} from $formdata{'state'} is";
print "<p>$formdata{'item'}</p>";
print "<p>Thanks. It's on its way.</p>";
print "</body></html>";
