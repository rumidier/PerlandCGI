#!/usr/bin/env perl
use Dancer;
use Metshe::Web;
use Plack::Builder;
my $app = dance;
builder {
  enable 'ReverseProxy';
  $app;
};

