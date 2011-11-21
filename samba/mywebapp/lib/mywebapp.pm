package mywebapp;

use 5.014;
use warnings;
use strict;
use Passwd::Unix;
use Unix::GroupFile;
use Template;
use Data::Dumper;
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
    my $groups   = param('l_group');

#
# groups가 NULL 인지 비교한후 NULL이 아니면 문자열 인지, arry ref 인지
# 확인하여 처리한다. 
#
    if (defined $groups) {
        if (ref($groups) eq 'ARRAY') {
            debug ref($groups);
        }
        elsif (!ref($groups)) {
            debug "----------  DEBUG -------------";
        }
    }

    template 'add', {
        u_id     => $u_id,
        u_name   => $u_name,
        u_passwd => $u_passwd,
        d_group  => $d_group,
        a_group  => $a_group,
    };

};

=pod
sub mk_dir {
    my $id = shift;
    mkdir "/home/s-rumidier/$id";
};

sub user_add {
    my ($id, $passwd, $name) = @_;
    my $pu = Passwd::Unix->new();

    my $err = $pu->user(
		    $id,
		    $pu->encpass($passwd),
		    $pu->maxuid + 1,
		    $pu->maxuid + 1,
		    $name,
		    "/home/s-rumidier/$id",
		    "/sbin/nologin"
		    ); 

    mk_dir($id);
};

sub group_add {
    my $id = shift;
    my @group = @_;
    my $grp = new Unix::GroupFile "/etc/group";
    $grp->add_usr("cv", $id);

    for ( 0 .. $#group ) {
        $grp->add_usr($group[$_], $id);
    }
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
