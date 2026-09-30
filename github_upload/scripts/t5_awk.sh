#!/bin/bash
awk -F',' 'NR>1 {print $15","$0}' data.csv | sort -t',' -k1 -nr | head -10 | cut -d',' -f2-
