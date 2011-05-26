#!/usr/bin/env perl

use strict;
use warnings;

my @pairs;
my %formdata;

if ($ENV{'REQUEST_METHOD'} eq 'GET') {
    @pairs = split (/&/, $ENV{'QUERY_STRING'});
}
elsif ($ENV{'REQUEST_METHOD'} eq 'POST') {
    my $buffer;
    read (STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    @pairs = split (/&/, $buffer);
}
else {
    print "Content-type: text/html\n\n";
    print "<p>Use Post or Get";
}

foreach my $pair (@pairs) {
    my ($key, $value) = split (/=/, $pair);
    $key =~ tr/+/ /;
    $key =~ s/%([a-fA-F0-9][a-fA-F09])/pack ("C", hex($1))/eg;
    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

    $value =~ s/<!--(.|\n)*-->//g;

    if ($formdata{$key}) {
        $formdata{$key} .= ", $value";
    }
    else
    {
        $formdata{$key} = $value;
    }
}

print "Content-type: text/html\n\n";
foreach my $key (sort keys (%formdata)) {
    print "<p>The field named <b>$key</b>
        contained <b>$formdata{$key}</b>";
}
