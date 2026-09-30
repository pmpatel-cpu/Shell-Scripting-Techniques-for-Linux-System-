import subprocess, time, statistics, json, os, sys

os.chdir('/home/claude/scripts')
RESULTS_FILE = '/home/claude/bench_results.json'

if os.path.exists(RESULTS_FILE):
    results = json.load(open(RESULTS_FILE))
else:
    results = {}

def bench(task, tech, cmd, runs, timeout=60):
    results.setdefault(task, {})
    times = []
    for i in range(runs):
        t0 = time.perf_counter()
        try:
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=timeout)
        except subprocess.TimeoutExpired:
            print(f"TIMEOUT: {task} {tech} run {i}")
            results[task][tech] = {"mean": None, "note": f"timeout>{timeout}s"}
            json.dump(results, open(RESULTS_FILE,'w'), indent=2)
            return
        t1 = time.perf_counter()
        times.append(t1 - t0)
    results[task][tech] = {
        "mean": statistics.mean(times),
        "min": min(times),
        "max": max(times),
        "stdev": statistics.stdev(times) if len(times) > 1 else 0.0,
        "runs": runs,
    }
    json.dump(results, open(RESULTS_FILE,'w'), indent=2)
    print(f"{task:30s} {tech:10s} mean={results[task][tech]['mean']:.4f}s ({runs} runs)")

# args: task tech cmd... runs timeout
task = sys.argv[1]
tech = sys.argv[2]
runs = int(sys.argv[3])
timeout = int(sys.argv[4])
cmd = sys.argv[5:]
bench(task, tech, cmd, runs, timeout)
