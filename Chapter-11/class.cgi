#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();
print "Content-type: text/html\n\n";

my $number = $formdata{'number'};

my %catalan = (1, "un", 2, "dos", 3, "tres", 4, "quatre", 5, "cinc");
my %spanish = (1, "uno", 2, "dos", 3, "tres", 4, "cuatro", 5, "cinco");
my %french = (1, "un", 2, "duex", 3, "trois", 4, "quatre", 5, "cinc");

if ($number =~/^[1-5]$/) {
    print "<p>you chose the number $number. Thar number translated into
        Catalanis <b>$catalan{$number}</b>. InFrench,
        it's <b>$french{$number}.</b>. In Spanish,
        it's <b>$spanish{$number}</b>.";
} else {
    print "<p>Sorry, you didn;t chosse a number between 1 and 5. Try again.";
}
