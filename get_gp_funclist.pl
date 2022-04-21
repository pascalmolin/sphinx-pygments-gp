#!/usr/bin/perl
use strict;
my %D;
for(<>) {
  chomp;
  #s/^(.*)functions\/// or continue;
  s/^(.*?)functions\///;
  my @f = split '/';
  push @{ $D{$f[0]} }, $f[1];
}
#delete $D{'symbolic_operators'};
print "gpkeywords = {\n";
foreach (keys %D) {
  @_ = @{$D{$_}}; shift @_;
  print "'$_' : \n";
  print "[ '", (join "', '", @_), "' ],\n" ;
}
print "}\n";
