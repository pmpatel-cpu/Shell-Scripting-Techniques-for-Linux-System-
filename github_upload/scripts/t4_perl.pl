#!/usr/bin/perl
use strict; use warnings;
open(my $fh, '<', 'data.csv') or die;
<$fh>;
my $n=0;
while (<$fh>) {
  my @f = split(',', $_);
  $n++ if $f[20] > 15;
}
print "$n\n";
