#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

print "Content-type: text/html\n\n";
print <<"HTML code";

<html>
  <head>
    <title>Showing off with HTML</title>
  </head>
  <body>
    <h2>Thanks for responding. Here's what you told us:</h2>
    <table border=3 width=60%>
      <tr><th>Key</th><th>value</th></tr>
HTML code

foreach my $key (keys %formdata) {
    print "<tr><td>$key</td><td>$formdata{$key}</td>\n";
}

print <<"HTML code2";
    </table>
  </body>
</html>
HTML code2
