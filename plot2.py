import matplotlib.pyplot as plt
import csv
name = "output/HD_ER_0.5_1e+04_1.csv"
name2 = "output/HD_ER_0.5_1e+04_5.csv"
smooth = [4]
ks = [0.5,1,2]
typ = ['ER', 'BAR', 'WS']
names = [f"output/HD_ER_{t}_1e+04_5.csv" for t in ks]

for name in names:
    with open(name) as f:
        val = list(csv.reader(f))
        f_val = [float(k[0]) for k in val]
        p_val = [float(k[1]) for k in val]
        plt.plot(f_val, p_val)
plt.legend(['k=0.5','k=1', 'k=2'])
plt.show()

ks = [2,4]
names = [f"output/HD_BAR_{t}_1e+04_1.csv" for t in ks]
names.append("output/HD_BAR_2_1e+04_5.csv")
for name in names:
    with open(name) as f:
        val = list(csv.reader(f))
        f_val = [float(k[0]) for k in val]
        p_val = [float(k[1]) for k in val]
        plt.plot(f_val, p_val)
plt.legend(['k=2','k=4'])
plt.show()

plt.figure()
ks = [2,4]
names = [f"output/HD_WS_{t}_1e+04_1.csv" for t in ks]
for name in names:
    with open(name) as f:
        val = list(csv.reader(f))
        f_val = [float(k[0]) for k in val]
        p_val = [float(k[1]) for k in val]
        plt.plot(f_val, p_val)
plt.legend(['k=2','k=4'])
plt.show()