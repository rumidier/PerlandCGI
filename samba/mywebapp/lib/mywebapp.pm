package mywebapp;

use lib 'lib';

use 5.014;
use utf8;
use warnings;
use strict;
use Passwd::Unix;
use File::Path qw/ make_path remove_tree /;
use Unix::GroupFile;
use Template;
use Data::Dumper;
use Dancer ':syntax';
use Encode;

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
    my $groups   = param('l_group');


    if ( defined(check_uid( $u_id )) ) {
        user_add( $u_id, $u_passwd, $u_name, $groups );

        template 'add',
                 {
                     u_id     => $u_id,
                     u_name   => $u_name,
                     u_passwd => $u_passwd,
                 };
    }
    else {
        template '/del_err',
                 {
                     u_id     => $u_id,
                     u_name   => $u_name,
                 };
    }

};

get '/del' => sub {
    template 'del';
};

post '/del' => sub {
    my $u_id = param('u_id');

    template 'del';
    user_del($u_id);
};

post '/del_err' => sub {
};

sub mk_dir {
    my ( $id, $uid ) = @_;

    make_path(
        "/home/$id",
        {
            owner => $id,
            group => 'cv',
            mode  => 0700
        }
    );
}

sub rm_dir {
    my $id = shift;

    remove_tree(
        "/home/$id",
        {
            owner => "$id",
            group => "cv",
            mode  => 0700
        }
    );
}

sub ug_del {
    my $id = shift;

    my $grp =Unix::GroupFile->new("/etc/group");

    $grp->remove_user("*", "$id");
}

sub user_add {
    my ( $id, $passwd, $name, $groups ) = @_;
    my $pu  = Passwd::Unix->new();
    my $grp = Unix::GroupFile->new("/etc/group");

    my $err = $pu->user(
        $id,
        $pu->encpass($passwd),
        $pu->maxuid + 1,
        $grp->gid('cv'),
        decode_utf8("$name"),
        "/home/$id",
        "/sbin/nologin"
    );

    if ( defined $groups ) {
        if ( ref($groups) eq 'ARRAY' ) {
            my $group_count = @{$groups} - 1;

            for ( 0 .. $group_count ) {
                $grp->add_user( "$groups->[$_]", $id );
            }
        }
        elsif ( !ref($groups) ) {
            $grp->add_user( $groups, $id );
        }

        $grp->commit();
        undef $grp;
    }

    mk_dir("$id");
}

sub user_del {
    my @users = qw/
      rumidier
      rumidier-test
      rumidier-test1
      rumidier-test2
      rumidier-test3
      rumidier-test4
      rumidier-test5
      rumidier-test6
      rumidier-test7
      rumidier-test8
      rumidier-test11
      rumidier-full-test
      rumidier-test-16
      rmidier-test-16-2
      whgksdud
      /;

    my ($id) = @_;

    my $pu = Passwd::Unix->new();

    given ($id) {
        when (@users) {
            $pu->del($_);
            rm_dir($_);
            ug_del($_);
        }
    }
}

sub check_uid {
    my $id = shift;
    my $pu = Passwd::Unix->new();

    my $uid = $pu->uid($id);
    debug "---------------------\n";
    debug "---------------------\n";
    debug "---------------------\n";
    debug "---------------------\n";
    unless ( defined($uid) ) {
        debug "---: uid not defined\n";
    }
    else {
        debug "uid :    $uid\n";
    }
    debug "---------------------\n";
    debug "---------------------\n";
    debug "---------------------\n";
    debug "---------------------\n";
}

true;
