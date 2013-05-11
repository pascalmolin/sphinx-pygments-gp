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
print "gpkeywords = {\n";
foreach (keys %D) {
  print "'$_' : \n";
  print "[ '", (join "', '", @{$D{$_}}), "' ],\n" ;
}
print "}\n";
