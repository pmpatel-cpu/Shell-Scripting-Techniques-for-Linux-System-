#!/bin/bash
awk -F',' 'NR>1 {sum[$3]+=$8; cnt[$3]++} END {for (k in sum) printf "%s: %.2f\n", k, sum[k]/cnt[k]}' data.csv
