#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
my @days = qw(Sunday Monday Tuesday Wednesday Thursday Friday Saturday);
my @months = qw(January February March April May June July August September October November Deember);

print "Content-type: text/html\n\n";

print <<"HTML code";

<html>
  <head>
     <title>Get the date</title>
  </head>
  <body>
     <p>Today is <b>$days[$wday], $months[$mon] $mday</b>
  </body>
</html>
HTML code
