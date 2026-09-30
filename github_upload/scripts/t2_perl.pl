#!/usr/bin/perl
use strict; use warnings;
open(my $fh, '<', 'data.csv') or die;
open(my $out, '>', '/tmp/t2_out.txt') or die;
<$fh>;
my $n=0;
while (<$fh>) {
  my @f = split(',', $_);
  if ($f[3] eq 'Critical') { print $out $_; $n++; }
}
print "$n\n";
