#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

my $comments = $formdata{'comments'};

    print "Content-type: text/html\n\n";
    print "??\n";
#open ( my $log, '>>', 'logfile.txt' )
#print {$log} "$comments\n";

#close($log);

print "<p>You commented thusly: <blokquote><p><i>$comments</i></blockquote>\n";
print "<hr />Would you like to see all the messages? <a
href=\"http://localhost/~rumidier/PerlandCGI/Chapter-14/readfromlog.cgi\">Yes</a>";

sub ErrorMessage {
    print "Content-type: text/html\n\n";
    print "The server can't open the file. It either doesn't exist or the permissions are wrong. \n";
    exit;
}
