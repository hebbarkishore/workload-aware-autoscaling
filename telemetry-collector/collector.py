
import csv
import time

with open('/data/metrics.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp","cpu","rps","latency"])
    for i in range(20):
        writer.writerow([time.time(), 0.4 + i*0.01, 100+i*5, 200-i])
        time.sleep(1)
