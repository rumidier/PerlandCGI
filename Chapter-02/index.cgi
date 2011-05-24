#!/usr/bin/perl

use strict;
use warnings;
use CGI;

my $q = CGI->new;

print $q->header;
print $q->start_html( "just cgi test" );
print $q->h1( "Hello CGI!" );
print $q->end_html;
