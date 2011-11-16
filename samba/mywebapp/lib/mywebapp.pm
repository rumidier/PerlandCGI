package mywebapp;
use Template;
use Unix::GroupFile;
use Dancer ':syntax';

our $VERSION = '0.1';

get '/' => sub {
    template 'index';
};

any '/test' => sub {
    template 'test';
};

get '/select' => sub {
    template 'select', {
        u_add => '/add',
        u_del => '/u_del',
    };
};

get '/add' => sub {
    template 'add', {
        action   => 'add',
    };
};

post '/add' => sub {
    my $u_id     = param('u_id');
    my $u_name   = param('u_name');
    my $u_passwd = param('passwd');
    my $d_group  = param('d_group');
    my $a_group  = param('a_group');

    template 'add', {
        u_id     => $u_id,
        u_name   => $u_name,
        u_passwd => $u_passwd,
        d_group  => $d_group,
        a_group  => $a_group,
    };
};

post '/sum' => sub {
    "I say a number:".params->{number};
};

=pod
get '/add' => sub {
    template 'test', {
        action => '/add',
        num1   => 0,
        num2   => 0,
        sum    => 0,
    };
};

post '/add' => sub {
    my $num1 = param('num-1') || 0;
    my $num2 = param('num-2') || 0;
    template 'test', {
        action  => '/add',
        num1    => $num1,
        num2    => $num2,
#        sum     => $num1 + $num2,
    };
};
=cut
true;
