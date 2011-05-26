#!/usr/bin/env perl

use strict;
use warnings;

my $rate = 55;
my $distance = 400;
my $driver = "Marion";
my $destination = "42 Indy Place";

my $name = $driver;

print "Content-type: text/html\n\n";
print "The rate is $rate, the distance is $distance, the driver is $driver,
      the destination is $destination. And the driver's name really is $name";
