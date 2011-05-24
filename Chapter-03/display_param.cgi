#!/usr/bin/env perl

use CGI ':standard';
@param=param();

print "Content-type: text/html\n\n";


foreach $name (param()) {
    @value= param($name);
    print "<P>The field with the NAME attribute equal to <B>$name</B> had
        a VALUE equal to <B>@value</B></P>\n";
}
