#!/usr/bin/env perl

use strict;
use warnings;
use lib '/home/rumidier/workspace/github/PerlandCGI/Chapter-09';
use Rumidier::SubParse::Subroutines;


#&mime;
#Rumidier::SubParse::Subroutines->mime();
Rumidier::SubParse::Subroutines::mime();
#&header ("This is the page title");
#Rumidier::SubParse::Subroutines->header("This is the page title");
Rumidier::SubParse::Subroutines::header("This is the page title");

print "This is more of that page wholly created by CGI and perl!";

#my $capped_which = Rumidier::SubParse::Subroutines->cap(Rumidier::SubParse::Subroutines->which());
my $capped_which =
Rumidier::SubParse::Subroutines::cap(Rumidier::SubParse::Subroutines::which());
#my $capped_which = &cap (&which);
print "<p>You\'rebrowsing this page with $capped_which</p>";

#Rumidier::SubParse::Subroutines->footer();
Rumidier::SubParse::Subroutines::footer();
#footer();
