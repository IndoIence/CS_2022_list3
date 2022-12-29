import matplotlib.pyplot as plt
import csv

def plot_save_one(fname: str):
    with open("output/" + fname) as file:
        ff = dict(csv.reader(file))
        x = list(map(float, ff.keys()))
        y = list(map(float, ff.values()))

    print(x)
    plt.plot(x, y)
    plt.savefig("plots/plot_" + fname[:-4] + ".png")
    plt.show()


def plot_mult( *names):
    # plt.figure(figsize=)
    for n in names:
        with open("output/" + n) as file:
            ff = dict(csv.reader(file))
            x = list(map(float, ff.keys()))
            y = list(map(float, ff.values()))
        plt.plot(x, y)



fname_bar2 = "GC_BAR_2_1e+04_10.csv"
fname_bar4 = "GC_BAR_4_1e+04_10.csv"
fname_ws2 = "GC_WS_2_1e+04_10.csv"
fname_ws4 = "GC_WS_4_1e+04_10.csv"
fname_05 = "GC_ER_0.5_1e+04_10.csv"
fname_1 = "GC_ER_1_1e+04_10.csv"
fname_2 = "GC_ER_2_1e+04_10.csv"
fname_4 = "GC_ER_4_1e+04_10.csv"
fnames = [fname_bar2, fname_bar4, fname_ws2, fname_ws4, fname_05, fname_1, fname_2, fname_4]
fnames_er = ["GC_ER_0.5_1e+04_100.csv", fname_1, fname_2, fname_4]
fnames_bar = [fname_bar2, fname_bar4]
fnames_ws = [fname_ws2, fname_ws4]

plot_save_one(fname_ws2)
for name in fnames:
    plot_save_one(name)
print(fname_4[:-4])
# ---------------- ER PLOT --------------------------
fnames_er_dict = {str(i): fnames_er[i] for i in range(len(fnames_er))}
plot_mult(*fnames_er_dict.values())
output_name = 'GC_ER'
plt.legend(['k=0.5', 'k=1', 'k=2', 'k=4'])
plt.title("Erdos-Renyi")
plt.xlabel("ratio of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()

# ---------------- BARABASSI PLOT --------------------------
fnames_bar_dict = {str(i): fnames_bar[i] for i in range(len([fname_bar2, fname_bar4]))}
plot_mult( *fnames_bar_dict.values())
output_name = 'GC_BAR'
plt.legend(['k=2', 'k=4'])
plt.title("Barabasi-Albert")
plt.xlabel("ratio of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()



# ---------------- WS PLOT --------------------------
fnames_ws_dict = {str(i): fnames_ws[i] for i in range(len([fname_ws2, fname_ws4]))}
plot_mult( *fnames_ws_dict.values())
output_name = 'GC_WS'
plt.legend(['k=2', 'k=4'])
plt.title("Watts Strogatz")
plt.xlabel("ratio of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()



gc2 = [fname_2, fname_ws2, fname_bar2]
plot_mult( *gc2)
plt.show()
gc4 = [fname_4, fname_ws4, fname_bar4]
plot_mult( *gc4)
plt.show()

hd = ['HD'+ f[2:] for f in fnames]
hd_er = hd[-4:]
hd_ws = hd[2:4]
hd_bar = hd[:2]
# ---------------- ER PLOT --------------------------
plot_mult(*hd_er)
output_name = 'HD_ER'
plt.legend(['k=0.5', 'k=1', 'k=2', 'k=4'])
plt.title("Erdos-Renyi")
plt.xlabel("number of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()


# ---------------- BAR PLOT --------------------------
plot_mult(*hd_bar)
output_name = 'HD_BAR'
plt.legend(['k=2', 'k=4'])

plt.title("Barabasi-Albert")
plt.xlabel("number of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()


# ---------------- WS PLOT --------------------------
plot_mult(*hd_ws)
output_name = 'HD_WS'
plt.legend(['k=2', 'k=4'])
plt.title("Watts Strogatz")
plt.xlabel("number of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()



cl = ['CL'+ f[2:].replace('+04','+03') for f in fnames]
cl_er = cl[-4:]
cl_ws = cl[2:4]
cl_bar = cl[:2]

# ---------------- ER PLOT --------------------------
plot_mult(*cl_er)
output_name = 'CL_ER'
plt.legend(['k=0.5', 'k=1', 'k=2', 'k=4'])
plt.title("Erdos-Renyi")
plt.xlabel("number of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()


# ---------------- BAR PLOT --------------------------
plot_mult(*cl_bar)
output_name = 'CL_BAR'
plt.legend(['k=2', 'k=4'])

plt.title("Barabasi-Albert")
plt.xlabel("number of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()
# ---------------- WS PLOT --------------------------
plot_mult(*cl_ws)
output_name = 'CL_WS'
plt.legend(['k=2', 'k=4'])
plt.title("Watts Strogatz")
plt.xlabel("number of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()

# ---------------- compare attack methods --------------------------
# this is terrible
plot_mult("GC_ER_2_1e+04_10.csv","HD_ER_2_1e+04_10.csv")
output_name = 'CL_WS'
plt.legend(['k=2', 'k=4'])
plt.title("Watts Strogatz")
plt.xlabel("number of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()

# ---------------- compare averaging methods --------------------------
plot_mult("GC_ER_0.5_1e+04_1.csv","GC_ER_0.5_1e+04_5.csv","GC_ER_0.5_1e+04_10.csv","GC_ER_0.5_1e+04_100.csv")
output_name = 'compare averaging methods'
plt.legend(['1','5', '10', '100'])
plt.title("")
plt.xlabel("ratio of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()

# ---------------- compare graph types random attack --------------------------
plot_mult("GC_ER_2_1e+04_10.csv","GC_WS_2_1e+04_10.csv","GC_BAR_2_1e+04_10.csv")
output_name = 'compare graph types random attack'
plt.legend(['Erdös-Rényi', 'Watts-Strogatz','Barabasi-Albert'])
plt.title("")
plt.xlabel("ratio of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()


# ---------------- compare graph types higest degree--------------------------
plot_mult("HD_ER_2_1e+04_10.csv","HD_WS_2_1e+04_10.csv","HD_BAR_2_1e+04_10.csv")
output_name = 'compare graph types higest degree'
plt.legend(['Erdös-Rényi', 'Watts-Strogatz','Barabasi-Albert'])
plt.title("")
plt.xlabel("number of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()

# ---------------- compare graph types higest degree--------------------------
plot_mult("CL_ER_2_1e+03_10.csv","CL_WS_2_1e+03_10.csv","CL_BAR_2_1e+03_10.csv")
output_name = 'compare graph types closeness'
plt.legend(['Erdös-Rényi', 'Watts-Strogatz','Barabasi-Albert'])
plt.title("")
plt.xlabel("number of removed nodes")
plt.ylabel(r"$\frac{P_{f}}{P_{0}}$", rotation = 0, fontsize = 15)
plt.savefig('plots/' + output_name)
plt.show()