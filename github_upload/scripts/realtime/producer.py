import sys, time, csv

src, live_log, producer_log, n_lines, interval = sys.argv[1:6]
n_lines = int(n_lines)
interval = float(interval)

with open(src) as f:
    r = csv.reader(f)
    header = next(r)
    rows = [row for _, row in zip(range(n_lines), r)]

out = open(live_log, 'a', buffering=1)   # line-buffered
plog = open(producer_log, 'a', buffering=1)

for row in rows:
    line = ','.join(row)
    t = time.time()
    out.write(line + '\n')
    out.flush()
    anomaly_id = row[1]
    plog.write(f"{anomaly_id},{t}\n")
    plog.flush()
    time.sleep(interval)

out.close()
plog.close()
# sentinel so consumers can exit gracefully without needing to be killed
with open(live_log, 'a', buffering=1) as f:
    f.write("__STOP__\n")
print(f"producer done: {len(rows)} lines written", file=sys.stderr)
