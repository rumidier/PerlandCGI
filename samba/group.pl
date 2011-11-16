#!/usr/bin/env perl 

use 5.010;
use strict;
use warnings;
use Unix::GroupFile;

my $grp = new Unix::GroupFile "/etc/group";
my $gid = $grp->maxgid;
$gid++;

print "sudo groupadd -g $gid bv_cath";
print "\n";
$gid++;
print "sudo groupadd -g $gid cv_cath";
print "\n";
$gid++;
print "sudo groupadd -g $gid dv_cath";
print "\n";
undef $grp;
