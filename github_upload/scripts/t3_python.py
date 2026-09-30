import csv
from collections import defaultdict
sums = defaultdict(int); cnts = defaultdict(int)
with open('data.csv') as f:
    r = csv.reader(f)
    next(r)
    for row in r:
        sums[row[2]] += int(row[7])
        cnts[row[2]] += 1
for k in sums:
    print(f"{k}: {sums[k]/cnts[k]:.2f}")
