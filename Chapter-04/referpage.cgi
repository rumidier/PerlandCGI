#!/usr/bin/env perl

print "Content-type: text/html\n\n";
print "<p>Before coming to this page, you were looking at
        $ENV{'HTTP_REFERER'}";
