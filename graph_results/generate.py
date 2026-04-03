import csv
import matplotlib.pyplot as plt

sizes = list()
times = list()

with open("results/runtimes.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sizes.append(int(row["length_a"]))
        times.append(float(row["runtime_ms"]))

plt.plot(sizes, times, marker='o')

plt.xlabel("String Length")
plt.ylabel("Runtime (ms)")
plt.title("String Input Size vs.HVLCS Runtime")

plt.grid(True)

plt.savefig("results/runtime_graph.png")
plt.show()