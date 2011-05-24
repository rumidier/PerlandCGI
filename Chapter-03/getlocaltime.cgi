#!/usr/bin/perl 

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst)=gmtime(time);

my %zones = ("EST", 5, "CT", 6, "MT", 7, "PT", 8);
my $place=$formdata{'place'};
my $zone=$formdata{'zone'};
$hour=$hour-$zones{$zone};

if ($hour <= 0){
        $hour = $hour + 24;
        }
$min = sprintf ("%02d", $min);
$sec = sprintf ("%02d", $sec);

print "Content-type: text/html\n\n";
print "According to my server, right now the time in $place is: $hour :$min
:$sec";
