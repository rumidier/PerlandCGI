#!/usr/bin/env perl 

use 5.014;
use strict;
use warnings;
use Passwd::Unix;

my $pu = Passwd::Unix->new();

foreach my $user ($pu->users) {
    print "Username: $user\nFull Name: ", $pu->gecos($user), "\n\n";
}

my @group = $pu->groups();

say "@group";
