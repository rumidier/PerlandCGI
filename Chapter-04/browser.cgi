#!/usr/bin/env perl

print "Content-type: text/html\n\n";
print "<p>The browser yoy're using to view this page is:
      $ENV{'HTTP_USER_AGENT'}";
