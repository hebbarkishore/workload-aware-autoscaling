
import csv

with open('/data/metrics.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

avg_cpu = sum(float(r['cpu']) for r in rows) / len(rows)
with open('/data/features.csv', 'w') as f:
    f.write("avg_cpu\n")
    f.write(str(avg_cpu))
