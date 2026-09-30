#!/usr/bin/perl
use strict; use warnings;
my %c;
open(my $fh, '<', 'data.csv') or die;
<$fh>;
while (<$fh>) {
  my @f = split(',', $_);
  $c{$f[3]}++;
}
for my $k (keys %c) { print "$k: $c{$k}\n"; }
