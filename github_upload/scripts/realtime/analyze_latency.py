import csv, statistics, json, glob, os

os.chdir('/home/claude/scripts/rt')

techniques = {
    'Bash (naive fork loop)': ('consumer_out_Bash.csv', 'producer_log_Bash.csv'),
    'Bash (pure builtin)': ('consumer_out_BashBuiltin.csv', 'producer_log_BashBuiltin.csv'),
    'Grep': ('consumer_out_Grep.csv', 'producer_log_Grep.csv'),
    'Awk': ('consumer_out_Awk.csv', 'producer_log_Awk.csv'),
    'Perl': ('consumer_out_Perl.csv', 'producer_log_Perl.csv'),
    'Python (polling)': ('consumer_out_PythonPoll.csv', 'producer_log_PythonPoll.csv'),
}

results = {}
for tech, (fname, plog_name) in techniques.items():
    producer = {}
    with open(plog_name) as f:
        for line in f:
            aid, t = line.strip().split(',')
            producer[aid] = float(t)

    latencies = []
    detected_ids = set()
    with open(fname) as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) < 3:
                continue
            detect_time = float(parts[0])
            anomaly_id = parts[2]  # parts[1] is Timestamp field, parts[2] is Anomaly_ID
            detected_ids.add(anomaly_id)
            if anomaly_id in producer:
                lat_ms = (detect_time - producer[anomaly_id]) * 1000
                latencies.append(lat_ms)

    # ground truth critical ids from producer perspective: we don't have severity in producer_log,
    # so just report based on what was detected & matched
    results[tech] = {
        'count_detected': len(detected_ids),
        'mean_latency_ms': statistics.mean(latencies) if latencies else None,
        'median_latency_ms': statistics.median(latencies) if latencies else None,
        'p95_latency_ms': statistics.quantiles(latencies, n=20)[18] if len(latencies) > 20 else max(latencies) if latencies else None,
        'max_latency_ms': max(latencies) if latencies else None,
        'min_latency_ms': min(latencies) if latencies else None,
        'stdev_latency_ms': statistics.stdev(latencies) if len(latencies) > 1 else 0,
    }
    print(f"{tech:28s} n={len(latencies):4d}  mean={results[tech]['mean_latency_ms']:.2f}ms  "
          f"median={results[tech]['median_latency_ms']:.2f}ms  p95={results[tech]['p95_latency_ms']:.2f}ms  "
          f"max={results[tech]['max_latency_ms']:.2f}ms")

json.dump(results, open('/home/claude/rt_latency_results.json', 'w'), indent=2)
