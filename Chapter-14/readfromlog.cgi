#!/usr/bin/env perl

use strict;
use warnings;

open (LOG, "<~/PerlandCGI/Chapter-14/logfile.txt") || &ErrorMessage;

my @logmessages = <LOG>;
close (LOG);

print "Content-type: text/html\n\n";
my $n = 1;
print "<ul>Messages</ul>";
foreach my $message (@logmessages) {
    print "<li>Message # $n was $message\n";
    $n++;
}

sub ErrorMessage {
    print "Content-type: text/html\n\n";
    print "The server can't open the file. It either doesn't exist or the
        permissions are wrong. \n";
    exit;
}
