#!/bin/bash
awk -F',' 'NR>1 && $21>15 {c++} END {print c}' data.csv
