use Test::More tests => 2;
use strict;
use warnings;

# the order is important
use Metshe::Web;
use Dancer::Test;

route_exists [GET => '/login'], 'a route handler is defined for /login';
response_status_is ['GET' => '/login'], 200, 'response status is 200 for /';
