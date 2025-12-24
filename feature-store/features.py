import csv

input_path = "/data/metrics.csv"
output_path = "/data/features.csv"

total_cpu = 0.0
count = 0

with open(input_path, newline="") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        cpu = row.get("cpu")
        if cpu:  
            total_cpu += float(cpu)
            count += 1

avg_cpu = total_cpu / count if count else 0.0

with open(output_path, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["avg_cpu"])
    writer.writerow([avg_cpu])