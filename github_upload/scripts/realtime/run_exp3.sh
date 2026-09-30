#!/bin/bash
set -u
cd /home/claude/scripts/rt

TECH="$1"
FILTER_CMD="$2"
N_LINES="${3:-1000}"
INTERVAL="${4:-0.003}"

rm -f live_log.csv producer_log.csv "consumer_out_${TECH}.csv"
touch live_log.csv

python3 producer.py data.csv live_log.csv producer_log.csv "$N_LINES" "$INTERVAL" 2>/dev/null &
PRODUCER_PID=$!

tail -n +1 -f --pid="$PRODUCER_PID" live_log.csv \
  | grep -v --line-buffered '__STOP__' \
  | eval "$FILTER_CMD" \
  | python3 stamper.py > "consumer_out_${TECH}.csv"

cp producer_log.csv "producer_log_${TECH}.csv"
echo "=== $TECH done: $(wc -l < consumer_out_${TECH}.csv) detected ==="
