#!/bin/bash
> /tmp/t2_out.txt
while IFS=',' read -r line; do
  sev=$(echo "$line" | cut -d',' -f4)
  if [ "$sev" == "Critical" ]; then
    echo "$line" >> /tmp/t2_out.txt
  fi
done < <(tail -n +2 data.csv)
wc -l < /tmp/t2_out.txt
