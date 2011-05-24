#!/usr/bin/env perl 

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

print "Content-type: text/html\n\n";

if ($formdata{'infotype'} eq 'time') {
    my %zones = ( 'Hartford', 5, 'Dallas', 6, 'Denver', 7, 'Eureka', 8 );
    my $city = $formdata {'city'};

    my ($sec, $min, $hour, $mday, $mon, %year, $wday, $yday, $isdst) = gmtime (time);
    $hour = $hour - $zones {$city};

    if ($hour <= 0) {
        $hour = $hour + 24;
    }

    $min = sprintf ("%02d", $min);
    $sec = sprintf ("%02d", $sec);

    print "<p>The local time in $city is $hour :$min : $sec";
}
else
{
    print "<p>I haven't written that part of the program yet. Sorry.";
}
