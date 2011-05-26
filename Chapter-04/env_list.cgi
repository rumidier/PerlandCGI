#!/usr/bin/env perl

print "Content-type: text/html\n\n";
print "<html><head><title>Enviroment Variables</title></head><body>";

foreach my $env_var (keys %ENV) {
    print "<br />
        <font color=red>
        $env_var</font> is set to <font color=blue>
        $ENV{$env_var}</font>";
}
print "</body></html>";
