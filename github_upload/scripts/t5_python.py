import csv
with open('data.csv') as f:
    r = csv.reader(f)
    header = next(r)
    rows = list(r)
rows.sort(key=lambda x: float(x[14]), reverse=True)
for row in rows[:10]:
    print(','.join(row))
