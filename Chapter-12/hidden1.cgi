#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

print "Content-type: text/html\n\n";
print "<html>\n<head><title>Using Hidden Fields</title></head>\n<body>\n";
print "Thanks, $formdata{'name'}, for entering your personal data. Now you
can chosse which items you'd like to purchase.\n";

print "<form method=POST
action=\"http://localhost/~rumidier/PerlandCGI/Chapter-12/hidden2.cgi\">\n";
print "<br \/>Item <input type=text name=item>\n";

foreach my $key (keys %formdata) {
    print "<br \/><input type=hidden name=$key value=$formdata{$key}>\n";
}

print "<input type=submit value=\"Send order\">\n";
print "</form></body></html>\n";
