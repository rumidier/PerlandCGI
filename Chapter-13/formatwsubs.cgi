#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;
use lib '/home/rumidier/workspace/github/PerlandCGI/Chapter-13';
use header_footer;

my %formdata = Rumidier::SubParse::Form->parse();

my ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
my @days = qw(Sunday Monday Tuesday Wednesday Thursday Friday Saturday);
my @months = qw(January February March April May June July August September October November Deember);

header_footer::Header("Get the Date");
print "<p>Today is <b>$days[$wday], $months[$mon] $mday.</b></p>\n";
header_footer::Footer;
