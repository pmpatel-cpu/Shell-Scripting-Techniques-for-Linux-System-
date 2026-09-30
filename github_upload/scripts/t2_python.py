import csv
n = 0
with open('data.csv') as f, open('/tmp/t2_out.txt','w') as out:
    r = csv.reader(f)
    header = next(r)
    for row in r:
        if row[3] == 'Critical':
            out.write(','.join(row) + '\n')
            n += 1
print(n)
