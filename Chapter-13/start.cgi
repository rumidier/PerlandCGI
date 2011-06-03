#!/usr/bin/env perl

my strict;
my warnings;
my Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

print "Content-type: text/html\n\n";
