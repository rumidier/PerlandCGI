#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

print "Content-type: text/html\n\n";
my %formdata = Rumidier::SubParse::Form->parse();

my $phrase = $formdata{'phrase'};

if ($phrase =~ /e/) {
    print "<p>Sorry, that sentence did in fact have an e. I told you: it's
        harder than it seems.";
} else {
    print "<p>Congratulations, that sentence had no e. Quite a feat!";
}
