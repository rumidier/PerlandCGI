#!/usr/bin/env perl

use strict;
use warnings;
use Rumidier::SubParse::Form;

my %formdata = Rumidier::SubParse::Form->parse();

print "Content-type: text/html\n\n";

print <<"HTML code";
<html>
  <head>
    <title>Using the Base tag</title>
    <base href="http://localhost/~rumidier/PerlandCGI/Chapter-13/"> 
  </head>
  <body>
  <center><h1>Saint George Tours</h1>
  <p><img src="Santjord.gif"></p>
  <h2>Thanks for responding to our questionnaire.</h2>
  </center>
  </body>
  </html>
HTML code
