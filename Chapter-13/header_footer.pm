package header_footer;

use strict;
use warnings;

sub Header {
        print "Content-type: text/html\n\n";
        print "<html><head><title>";
        print "$_[0]";
        print "</title></head><body>\n";
}

sub Footer {
        print "\n</body></html>";
}
1;
