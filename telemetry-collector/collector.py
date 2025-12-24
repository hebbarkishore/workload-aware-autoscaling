import csv
import time
import os

FILE_PATH = "/data/metrics.csv"
ROWS = 20
INTERVAL_SECONDS = 1

file_exists = os.path.isfile(FILE_PATH)

with open(FILE_PATH, "a", newline="") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(["timestamp", "cpu", "rps", "latency"])

    for i in range(ROWS):
        writer.writerow([
            int(time.time()),
            round(0.4 + i * 0.01, 2),  
            100 + i * 5,              
            max(50, 200 - i)           
        ])
        f.flush()                     
        time.sleep(INTERVAL_SECONDS)