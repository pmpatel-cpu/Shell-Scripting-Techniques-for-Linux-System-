#!/bin/bash
declare -A sum cnt
while IFS=',' read -r -a f; do
  type="${f[2]}"; rt="${f[7]}"
  sum["$type"]=$(( ${sum["$type"]:-0} + rt ))
  cnt["$type"]=$(( ${cnt["$type"]:-0} + 1 ))
done < <(tail -n +2 data.csv)
for k in "${!sum[@]}"; do
  avg=$(( sum[$k] / cnt[$k] ))
  echo "$k: $avg"
done
