#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
my @classes = ("Latin 305", "Advanced Greek Grammar", "Applied Linguistics",
                 "Virgil and the Iliad");
my @newclasses = split (/,/, $formdata{'newclass'});
my @IDs = split(/,/, $formdata{'ID'});

print "Content-type: text/html\n\n";
print "<p><b>You replaced: </b></p>";

my $number;
foreach $number (@IDs) {
    $number--;
    print "<li>$classes[$number]</li>";
}

print "<p><b>with:</b></p> ";
my @newarray;
foreach my $course (@newclasses) {
    if ($course ne " ") {
        print "<li>$course</li>";
       @newarray = (@newarray, $course);
    }
}

@classes[@IDs] = @newarray;

print "<h2>Your complete list is now:</h2><ul>";
foreach my $item (@classes) {
    print "<li>$item</li>";
}
print "</ul>";
