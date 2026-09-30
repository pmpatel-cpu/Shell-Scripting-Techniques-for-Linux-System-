#!/bin/bash
awk -F',' 'NR>1 {c[$4]++} END {for (k in c) print k": "c[k]}' data.csv
