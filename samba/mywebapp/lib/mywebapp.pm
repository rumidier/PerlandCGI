package mywebapp;

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
use Encode 'from_to';

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

#
# groups가 NULL 인지 비교한후 NULL이 아니면 문자열 인지, arry ref 인지
# 확인하여 처리한다.
#
    user_add( $u_id, $u_passwd, $u_name, $groups );

    template 'add',
      {
        u_id     => $u_id,
        u_name   => $u_name,
        u_passwd => $u_passwd,
      };

};

get '/del' => sub {
    template 'del';
};

post '/del' => sub {
    my $u_id = param('u_id');

    template 'del';
    user_del($u_id);
};

=pod
sub mk_dir {
    my ( $id, $uid ) = @_;

    make_path(
        "/home/$id",
        {
            owner => $uid,
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
=cut

sub ug_del {
    my $id = shift;

    my $grp =Unix::GroupFile->new("/etc/group");

    $grp->remove_user("*", "$id");
}

sub user_add {
    my ( $id, $passwd, $name, $groups ) = @_;
    my $pu  = Passwd::Unix->new();
    my $grp = new Unix::GroupFile "/etc/group";

    debug "-----| name : $name |----\n";
    my $de_name = utf8::decode("$name");
    my $new_uid = $pu->maxuid + 1;
=pod
    my $err = $pu->user( $id, $pu->encpass($passwd), $new_uid,
        $grp->gid('cv'), $de_name, "/home/$id", "/sbin/nologin" );

    if ( !($err) ) {
        debug "------not user add\n\n\n\n";
    }

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

# mk_dir("$id", $new_uid);
=cut
}

sub user_del {
    my @users = qw/
      rumidier-test
      rumidier-test1
      rumidier-test2
      rumidier-test3
      rumidier-test4
      rumidier-test5
      rumidier-test6
      rumidier-test7
      rumidier-test11
      rumidier-test-16
      rmidier-test-16-2
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

true;
