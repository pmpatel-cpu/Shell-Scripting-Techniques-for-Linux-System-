#!/usr/bin/perl
use strict; use warnings;
open(my $fh, '<', 'data.csv') or die;
<$fh>;
my @rows;
while (<$fh>) {
  my @f = split(',', $_);
  push @rows, [$f[14], $_];
}
my @sorted = sort { $b->[0] <=> $a->[0] } @rows;
print $_->[1] for @sorted[0..9];
