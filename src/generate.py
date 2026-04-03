import csv
import matplotlib.pyplot as plt

sizes = list()
times = list()

with open("runtimes/runtimes.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sizes.append(int(row["length_a"]))
        times.append(float(row["runtime_ms"]))

plt.plot(sizes, times, marker='o')

plt.xlabel("String Length")
plt.ylabel("Runtime (ms)")
plt.title("Runtime of 10 Input Files")

plt.grid(True)

plt.savefig("runtimes/graph.png")
plt.show()