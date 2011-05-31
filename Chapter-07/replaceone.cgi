#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
my @classes = ("Latin 305", "Advanced Greek Grammar", "Applied Linguistics",
         "Virgil and the Iliad");
my @newclass = split (/,/, $formdata{'newclass'});
my $ID = $formdata{'ID'};

print "Content-type: text/html\n\n";
my $new_cl;
foreach $_ (@newclass) {
    if ($_ ne " ") {
        $new_cl = $_;
    }
}
print "<h2>You replaced $classes[$ID] with $new_cl. ";

$classes[$ID] = $new_cl;

print "Your complete list is now: </h2><ul>";

foreach my $item (@classes) {
    print "<li>$item</li>";
}
print "</ul>";
