package mywebapp;

use 5.014;
use Passwd::Unix;
use Template;
use Unix::GroupFile;
use Dancer ':syntax';

our $VERSION = '0.1';

get '/' => sub {
    template 'index';
};

get '/select' => sub {
    template 'select';
};

get '/add' => sub {
	template 'add';
};

post '/add' => sub {
    my $u_id     = param('u_id');
    my $u_name   = param('u_name');
    my $u_passwd = param('passwd');
    my $d_group  = param('d_group');
    my $a_group  = param('a_group');

    mkdir "/home/s-rumidier/$u_id";
=pod
    user_add ($u_id, $u_passwd, $u_name)
    group_add ($d_group, $a_group);
=cut
    template 'add', {
        u_id     => $u_id,
        u_name   => $u_name,
        u_passwd => $u_passwd,
        d_group  => $d_group,
        a_group  => $a_group,
    };

};

=pod
sub user_add {
    my $pu = Passwd::Unix->new();

    my $err = $pu->user($u_id, $pu->encpass($u_passwd), $pu->maxuid + 1, $pu->maxuid + 1,
$u_name, "/home/s-rumidier/$u_id", "/sbin/nologin"); 
    mkdir "/home/s-rumidier/$u_id";
};

sub group_add {
};

post '/sum' => sub {
    "I say a number:".params->{number};
};

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
        sum     => $num1 + $num2,
    };
};
=cut


true;
