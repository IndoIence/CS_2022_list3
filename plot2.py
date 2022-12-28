import matplotlib.pyplot as plt
import csv
name = "output/GC_BAR_0.5_1e+04_9.csv"
smooth = [8]
ks = [0.5,2,4]
type = ['ER', 'BAR', 'WS']
for v in smooth:
    for k in ks:
        name = f"output/GC_ER_{k}_1e+04_{v}.csv"
        with open(name) as f:
            val = list(csv.reader(f))
            f_val = [float(k[0]) for k in val]
            p_val = [float(k[1]) for k in val]
            plt.plot(f_val, p_val)

plt.show()