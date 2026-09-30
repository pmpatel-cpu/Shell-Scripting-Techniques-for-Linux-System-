import sys, time

for line in sys.stdin:
    t = time.time()
    sys.stdout.write(f"{t},{line}")
    sys.stdout.flush()
