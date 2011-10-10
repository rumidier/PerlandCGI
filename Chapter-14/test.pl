#!/usr/bin/perl 

use strict;
use warnings;

open ( my $hot, '>>', 'logfile' );
print {$hot} "Why internet....\n";
close $hot;
