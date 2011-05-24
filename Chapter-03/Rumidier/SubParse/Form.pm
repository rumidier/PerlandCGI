package Rumidier::SubParse::Form;

use strict;
use warnings;

print "Content-type: text/html\n\n";
foreach my $env_val (keys %ENV) {
  print "* $env_val : $ENV{$env_val}<br />\n";
}
sub parse {
    my @pairs;

    if ( $ENV{'REQUEST_METHOD'} eq 'GET' ) {
        @pairs = split( /&/, $ENV{'QUERY_STRING'} );
    }
    elsif ( $ENV{'REQUEST_METHOD'} eq 'POST' ) {
        my $buffer;
        read( STDIN, $buffer, $ENV{'CONTENT_LENGTH'} );
        @pairs = split( /&/, $buffer );

        if ( $ENV{'QUERY_STRING'} ) {
            my @getpairs = split( /&/, $ENV{'QUERY_STRING'} );
            push( @pairs, @getpairs );
        }
    }
    else {
        print "Content-type: text/html\n\n";
        print "<p>Use Post or Get";
    }

    my %formdata;
    foreach my $pair (@pairs) {
        my ( $key, $value ) = split( /=/, $pair );

        $key   =~ tr/+/ /;
        $key   =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
        $value =~ s/<!--(.|\n)*-->//g;

        if ( $formdata{$key} ) {
            $formdata{$key} .= ", $value";
        }
        else {
            $formdata{$key} = $value;
        }
    }

    return %formdata;
}

1;
