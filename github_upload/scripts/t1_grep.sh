#!/bin/bash
for sev in Low Medium High Critical; do
  n=$(grep -c ",$sev," data.csv)
  echo "$sev: $n"
done
