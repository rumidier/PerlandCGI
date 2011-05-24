#!/usr/bin/env perl 

use strict;
use warnings;

my( $sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst ) =
localtime(time);

$min=sprintf ( "%02d", $min );
$sec=sprintf ( "%02d", $sec );

print "Content-type: text/html\n\n";
print "According to my server, right now the time is: $hour :$min :$sec";
