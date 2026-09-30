import csv
n = 0
with open('data.csv') as f:
    r = csv.reader(f)
    next(r)
    for row in r:
        if int(row[20]) > 15:
            n += 1
print(n)
