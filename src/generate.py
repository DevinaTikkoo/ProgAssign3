import csv
import matplotlib.pyplot as plt

sizes = list()
times = list()

#read runtimes and populate sizes and times lists
with open("runtimes/runtimes.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sizes.append(int(row["length_a"]))
        times.append(float(row["runtime_ms"]))

#plot coordinate points
plt.plot(sizes, times, marker='o')

#label axes and title
plt.xlabel("String Length")
plt.ylabel("Runtime (ms)")
plt.title("Runtime of 10 Input Files")
plt.grid(True)
#save graph as png in runtimes folder 
plt.savefig("runtimes/graph.png")
plt.show()