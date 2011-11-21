#!/usr/bin/perl 
#===============================================================================
#
#         FILE:  g.pl
#
#        USAGE:  ./g.pl 
#
#  DESCRIPTION:  
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  2011년 11월 16일 22시 15분 02초 KST
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;


my $id = "N111623";

my $cmd1 = "/sbin/zfs create pool01/home/%s";
my $cmd2 = "/sbin/zfs set quota=1G pool01/home/%s";

my $cmd3 = "/usr/sbin/chown -R %s:cv /pool01/home/%s";
my $cmd4 = "/bin/chmod -R 700 /pool01/home/%s";

exec(sprintf $cmd1,$id);
