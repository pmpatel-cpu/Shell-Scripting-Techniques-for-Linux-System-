import sys, time

path = sys.argv[1]
poll_interval = float(sys.argv[2]) if len(sys.argv) > 2 else 0.005

f = open(path, 'r')
f.seek(0, 2)  # seek to end, like tail -f

while True:
    line = f.readline()
    if not line:
        time.sleep(poll_interval)
        continue
    if not line.endswith('\n'):
        # partial line, wait for the rest
        pos = f.tell()
        time.sleep(poll_interval)
        f.seek(pos)
        continue
    stripped = line.rstrip('\n')
    if stripped == '__STOP__':
        break
    fields = stripped.split(',')
    if len(fields) > 3 and fields[3] == 'Critical':
        sys.stdout.write(line)
        sys.stdout.flush()
