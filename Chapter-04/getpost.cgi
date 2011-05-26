#!/usr/bin/env perl

print "Content-type: text/html\n\n";

print "<p>The Reques method was:
    $ENV{'REQUEST_METHOD'}";

print "<p>the data from GET was:
    $ENV{'QUERY_STRING'}";

print "<p>The data from POST had
    $ENV{'CONTENT_LENGTH'}bytes. You can find it in
    standard input.";
