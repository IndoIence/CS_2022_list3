import matplotlib.pyplot as plt
import csv


def k_compare():
    plt.figure(figsize=(9, 6))
    for size in [1e3, 1e4]:
        for i in range(1, 11):
            f_name = f"output/giant_component_0.002_{i}_{size:.1g}.csv"
            with open(f_name) as f:
                file_vals = list(csv.reader(f))

            f_val = [float(k[0]) for k in file_vals]
            p_val = [float(k[1]) + i * 0.1 for k in file_vals]
            plt.plot(f_val, p_val)

        plt.legend([f"L={i}" for i in range(1, 11)])
        plt.yticks([])
        plt.savefig(f"L_compare_{size:.1g}")
        plt.show()


def plot_save(fname: str):
    with open("output/" + fname) as file:
        ff = dict(csv.reader(file))
        x = list(map(float, ff.keys()))
        y = list(map(float, ff.values()))

    print(x)
    plt.plot(x, y)
    plt.savefig("plots/plot_" + fname[:-4] + ".png")
    plt.show()


fname_bar2 = "GC_BR_4_1e+04_10.csv"
fname_bar4 = "GC_BR_4_1e+04_10.csv"
fname_ws4 = "GC_WS_4_1e+04_10.csv"
fname_ws2 = "GC_WS_2_1e+04_10.csv"
fname_05 = "GC_ER_0.5_1e+04_10.csv"
fname_1 = "GC_ER_1_1e+04_10.csv"
fname_2 = "GC_ER_2_1e+04_10.csv"
fname_4 = "GC_ER_4_1e+04_10.csv"
fnames = [fname_bar2, fname_bar4, fname_ws2, fname_ws4, fname_05, fname_1, fname_2, fname_4]
fnames = [fname_05, fname_1, fname_2, fname_4]
for name in fnames:
    plot_save(name)
print(fname_4[:-4])

for name in [fname_05, fname_1, fname_2, fname_4]:
    with open("output/"+name) as f:
        ff = dict(csv.reader(f))
    x = list(map(float, ff.keys()))
    y = list(map(float, ff.values()))
    plt.savefig("0.5.png")
    plt.plot(x,y)
plt.legend([fname_05, fname_1, fname_2, fname_4])
# plt.legend(["GC_ER_0.5_1e+04_10.csv", "GC_ER_1_1e+04_10.csv", fname_2, fname_4])
plt.show()

