#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
print "Set-cookie:language=formdata{'lnaguage'}\n";

print "Content-type: text/html\n\n";
print "<html><head><title>Thanks for choosing!</title></head><body>";
print "You chose $formdata{'language'}. Nest time you visit, I'll greet you
accordingly.";
