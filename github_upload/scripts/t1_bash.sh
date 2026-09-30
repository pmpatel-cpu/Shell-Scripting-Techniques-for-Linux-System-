#!/bin/bash
declare -A counts
while IFS=',' read -r -a f; do
  sev="${f[3]}"
  counts["$sev"]=$(( ${counts["$sev"]:-0} + 1 ))
done < <(tail -n +2 data.csv)
for k in "${!counts[@]}"; do echo "$k: ${counts[$k]}"; done
