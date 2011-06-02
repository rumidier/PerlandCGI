#!/usr/bin/env perl

use strict;
use warnings;

print "Content-type: text/html\n\n";
my $browser = $ENV{'HTTP_USER_AGENT'};

if ($browser =~ /MSIE/) {
    print "You're using IE";
} elsif ($browser =~ /Mozilla/) {
    print "You're using Netscape";
} else {
    print "You're using something else";
}

print "<hr /><font size=+1>";
print "<p>The environment variable was $browser</p>";

print "<p>\$& is $&</p>";
print "<p>\$` is $`</p>";
print "<p>\$' is $'</p>";
print "</font>";
