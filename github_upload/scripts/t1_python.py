import csv
from collections import Counter
c = Counter()
with open('data.csv') as f:
    r = csv.reader(f)
    next(r)
    for row in r:
        c[row[3]] += 1
for k,v in c.items():
    print(f"{k}: {v}")
