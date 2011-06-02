#!/usr/bin/env perl

use strict;
use warnings;

print "Content-type: text/html\n\n";

my $browser = $ENV{'HTTP_USER_AGENT'};

if ($browser =~ m/MSIE/) {
    print "You;re using IE";
} elsif ($browser =~ m/Mozilla/) {
    print "You're using Netscape";
} else {
    print "You're using somthing else";
}
