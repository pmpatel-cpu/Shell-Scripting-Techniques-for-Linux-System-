#!/bin/bash
awk -F',' 'NR>1 && $4=="Critical"' data.csv > /tmp/t2_out.txt
wc -l < /tmp/t2_out.txt
