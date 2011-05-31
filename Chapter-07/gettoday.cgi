#!/usr/bin/env perl

use strict;
use warnings;

my ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime (time);

my @days = qw(Sunday Monday Tuesday Wednesday Thursday Friday Saturday);
my @months = qw(January February March April May June July August September
        October November December);

my @catdays = qw(diumenge dilluns dimarts dimecres dijous divendres dissabte);
my @catmonths = qw(Gener Febrer Mar&#231\;
        Abril Maig Juny Juliol Agost Setembre Octubre Novembre Desembre);

my $eacute;
print "Content-type: text/html\n\n";
print "Today is $days[$wday], $months[$mon] $mday.";
print "<p>In Catalonia, they'd say: Avui $eacute\;s $catdays[$wday], $mday de
$catmonths[$mon].";

