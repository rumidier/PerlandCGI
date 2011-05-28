#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

print "Content-type: text/html\n\n";

my $counter = $formdata{'counter'};

++$counter;
print "Your number incremented by 1 is $counter";
my $watch = ++$counter;
print "<br />Your number, incremented again by 1, is now $counter. If we store
that operation, its value is also $watch.";

$counter = $formdata{'counter'};
print "<hr />Let's start over, with your original number $counter";
$counter++;
print "<br />Again, your number incremented by 1 is $counter";
$watch = $counter++;
print "<br />Now we store the value of yout number in a second variable, which
is now equal to $watch, and then we increment your number again. It's now
$counter.";
