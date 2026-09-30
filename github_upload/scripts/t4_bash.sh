#!/bin/bash
n=0
while IFS=',' read -r -a f; do
  if [ "${f[20]}" -gt 15 ]; then
    n=$((n+1))
  fi
done < <(tail -n +2 data.csv)
echo "$n"
