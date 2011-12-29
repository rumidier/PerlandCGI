package samba;

use lib 'lib';

use 5.010;
use utf8;
use warnings;
use strict;
use Passwd::Unix;
use File::Path qw/ make_path remove_tree /;
use Unix::GroupFile;
use Passwd::Samba;
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
    my $u_id       = param('u_id');
    my $u_name     = param('u_name');
    my $u_passwd   = param('passwd');
    my $sam_passwd = param('samba_passwd');
    my $groups     = param('l_group');

    my $uid_check  = uid_exist_check( $u_id );
    if ( $uid_check ) {
        template 'add',
        {
            u_id     => $u_id,
            string   => '가 현재 존재 합니다',
        };
    }
    else {
#       samba_user_add( $u_id, $sam_passwd );
#       <fh>가 열리지 않음
        my $user_add_value = user_add( $u_id, $u_passwd, $u_name, $groups );

        unless ( $user_add_value ) {
            user_del($u_id);
            template '/add',
            {
                u_id   => $u_id,
                string => '생성에 실패 하였습니다.',
            };
        }
        else {
            template 'add',
            {
                u_id     => $u_id,
                string   => '생성에 성공 하였습니다.',
            };
        }
    }
};

get '/del' => sub {
    template 'del';
};

post '/del' => sub {
    my $user_id = param('u_id');
    my $uid_exist_value = uid_exist_check( $user_id );

    if ( $uid_exist_value ) {
        my $uid_info = uid_get_info( $user_id );
        my $home_dir = $uid_info->{'home'};
        my @groups   = @{ $uid_info->{'groups'} };

        template 'info_view',
            {
                 u_id_test    => $user_id,
                 home_dir     => $home_dir,
                 groups       => \@groups,
            };
# $uid_exist_value 가 존재 하고 id에 존재 하는 홈폴더, gid등 연계된
# 부분에 대하여 출력한후 삭제 할것인지 재확인 
    }
    else {
        if ( $user_id ) {
    	    template 'del',
                {
                    u_id     => $user_id,
                    string   => '가 존재 하지 않습니다',
                };
        }
        else {
    	    template 'del',
                {
                    u_id     => 'ID',
                    string   => '를 입력해 주세요.',
                };
        }
    }
};

post '/del_active/:u_id_test?' => sub {
    my $user_id = param('u_id_test');
    if ( $user_id ) {
        my $user_del_value = user_del($user_id);

        if ( ($user_del_value) ) {
            template 'del',
            {
                u_id     => $user_id,
                string   => '삭제에 성공 하였습니다.',
            };
        }
        else {
            template 'del',
            {
                u_id     => $user_id,
               string   => '삭제에 실패 하였습니다.',
            };
        }
    }
};

sub mk_dir {
    my ( $id ) = @_;
    return 0 unless $id;

    my $make_path_success = make_path(
        "/home/$id",
        {
            owner => $id,
            group => 'cv',
            mode  => 0700
        }
    );
    return 0 unless $make_path_success;
}

sub rm_dir {
    my $id = shift;
    return 0 unless $id;

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
    return 0 unless $id;

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
    return 0 unless $err;

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

    my $mk_dir_success = mk_dir("$id");
    return 0 unless $mk_dir_success
}

sub user_del {
    my ($id) = @_;
    return 0 unless $id;

    my $pu = Passwd::Unix->new();

    my $user_del_value = $pu->del($id);
    return 0 unless ($user_del_value);
    my $dir_del_value  = rm_dir($id);
    return 0 unless ($dir_del_value);
    my $user_group_del_value  = ug_del($id);
    return 0 unless ($user_group_del_value);

    return 1;
}

sub uid_exist_check {
    my $id = shift;
    my $pu = Passwd::Unix->new();

    my $uid = $pu->uid($id);

    return 0 unless defined( $uid );

    return $uid;
}

sub samba_user_add {
    my ( $id, $sam_passwd ) = @_;

    my $ps  = Passwd::Samba->new();
    my $err = $ps->passwd( $id, $sam_passwd );

    foreach my $user ($ps->users) {
        print "Username: $user\nUID: ", $ps->uid($user), "\n\n";
    }
}

sub uid_get_info {
    my $user_id = shift;
    return 0 unless $user_id;

    my @user_info = getpwnam( $user_id );
    my $home_dir = $user_info[7];

    my @groups;
    while (my @ent = getgrent() ) {
        my @user = split " ", $ent[-1];
    
        if ($user_id ~~ @user) {
            push @groups, $ent[0];
        }
    }

    my %info = (
	    home   => $home_dir,
        groups => [@groups],
    );

    return \%info;
}

true;
