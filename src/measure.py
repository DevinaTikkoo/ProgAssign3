import subprocess
import time
import csv
import os

# Sizes of input strings a and b for test files test1 through test10
sizes = [25, 35, 55, 75, 95, 120, 145, 170, 200, 230]

measured_results = list()
#Run OPT on each file and measure run time
for index, size in enumerate(sizes, start=1):
    input_file = f"tests/question1/{index}.in"

    start_time = time.perf_counter()
    subprocess.run(["python", "src/main.py", input_file], capture_output=True, text=True)
    end_time = time.perf_counter()

    runtime_in_ms = (end_time - start_time) * 1000
    measured_results.append([f"test{index}.in", size, size, runtime_in_ms])

#Save results to CSV file for generate.py
with open("runtimes/runtimes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["file", "length_a", "length_b", "runtime_ms"])
    writer.writerows(measured_results)

#Print results/measured runtimes 
for row in measured_results:
    print(row)