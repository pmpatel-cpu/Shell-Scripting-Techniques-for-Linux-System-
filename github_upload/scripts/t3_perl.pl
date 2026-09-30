#!/usr/bin/perl
use strict; use warnings;
my (%sum, %cnt);
open(my $fh, '<', 'data.csv') or die;
<$fh>;
while (<$fh>) {
  my @f = split(',', $_);
  $sum{$f[2]} += $f[7];
  $cnt{$f[2]}++;
}
for my $k (keys %sum) {
  printf "%s: %.2f\n", $k, $sum{$k}/$cnt{$k};
}
