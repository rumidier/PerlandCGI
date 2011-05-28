#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my $base = $formdata{'base'};
my $school = $formdata{'school'};
my $cheer = $base x 2 . $school;

my $number = $formdata{'number'};
my $repeat = $formdata{'repeat'};
my $repeat_number = $number x $repeat;

print "Content-type: text/html\n\n";
print "<font size =+2>The cheer is<b>$cheer</b>.";
print "<p>And the number, $number, repeated $repeat times is
      <b>$cheer</b>.";
print "<p>And the number, $number, repeated $repeat times is
      <b>$repeat_number<b></font>";;
