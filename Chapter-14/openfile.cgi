#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my $comments = $formdata{'comments'};

open(LOG, ">>~/PerlandCGI/Chapter-14/logfile.txt") || &ErrorMessage;
print LOG "$comments\n";
close(LOG);

print "Content-type: text/html\n\n";
print "<p>You commented thusly:
<blockquote><p><i>$comments</i></p></blockquote>\n";
print "<hr />Would you like to see all the messages? <a
href=\"http://localhost/~rumidier/PerlandCGI/Chapter-14/readfromlog.cgi\">Yes</a>";

sub ErrorMessage {
    print "Content-type: text/html\n\n";
    print "The server can't open the file. It either doesn't exist or
        the permissions are wrong. \n";
    exit;
}
