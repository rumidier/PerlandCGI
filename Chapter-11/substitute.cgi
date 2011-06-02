#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

print "Content-type: text/html\n\n";

my $comments = $formdata{'comments'};

if ($comments =~ /<IMG[^>]*>/) {
    print "<p>Sorry, images are not permitted. please limit your comments to
        ntext.";
    $comments =~ s/<IMG[^>]*>//g;
}

print "<p>Your text comments were <p><b>$comments"
if
$comments;
