from graphType import GraphType
import networkx as nx
import numpy as np
import csv
import time

def first_part(size, ks, L_list, f_list):
    for L in L_list:
        for gr in ks:
            for k in gr.k_val:
                k_dict = {f: 0 for f in f_list}
                k_dict[0] = L
                for _ in range(L):
                    g_new = er.make_new(size, k)
                    giant_before = max(nx.connected_components(g_new), key=len)
                    # number of nodes to be removed every iteration
                    n = round(1 / p_numb * len(g_new.nodes()))
                    for f in f_list[1:]:
                        g_after = rand_remove(g_new, n)
                        giant_after = max(nx.connected_components(g_after), key=len)
                        k_dict[f] += len(giant_after) / len(giant_before)

                # title = f"output_old/GC_ws_{k}_{size:.1g}_{L}.csv"
                title = f"output/GC_{gr.name}_{k}_{size:.1g}_{L}.csv"
                to_csv(title, L, k_dict)


def second_part(size, ks, L_list):
    for L in L_list:
        for gr in ks:
            for k in gr.k_val:
                k_dict = {f: 0 for f in range(round(size*7/10))}
                for _ in range(L):
                    g_new = er.make_new(size, k)
                    giant_before = max(nx.connected_components(g_new), key=len)
                    not_all_nodes = round(len(g_new.nodes())*7/10) #removing last 30% of nodes
                    for f in range(not_all_nodes):
                        node_higest_degree = max(g_new.degree, key=lambda x: x[1])[0]
                        g_new.remove_node(node_higest_degree)
                        giant_after = max(nx.connected_components(g_new), key=len)
                        k_dict[f] += len(giant_after) / len(giant_before)

                # title = f"output_old/GC_ws_{k}_{size:.1g}_{L}.csv"
                title = f"output/HD_{gr.name}_{k}_{size:.1g}_{L}.csv"
                to_csv(title, L, k_dict)


def third_part_closeness(size, ks, L_list):
    for L in L_list:
        for gr in ks:
            for k in gr.k_val:
                k_dict = {f: 0 for f in range(round(size*9/10))}
                for _ in range(L):
                    g_new = er.make_new(size, k)
                    giant_before = max(nx.connected_components(g_new), key=len)
                    not_all_nodes = round(len(g_new.nodes())*9/10) # not removing last 10% of nodes
                    for f in range(not_all_nodes):
                        close = nx.closeness_centrality(g_new)
                        node_higest_centr = max(close.keys(), key=lambda x: close[x])
                        g_new.remove_node(node_higest_centr)
                        giant_after = max(nx.connected_components(g_new), key=len)
                        k_dict[f] += len(giant_after) / len(giant_before)

                # title = f"output_old/GC_ws_{k}_{size:.1g}_{L}.csv"
                title = f"output/CL_{gr.name}_{k}_{size:.1g}_{L}.csv"
                to_csv(title, L, k_dict)

def rand_remove(g: nx.classes.graph.Graph, node_nr: int):
    assert node_nr >= 0, "give a positive number of nodes to remove"
    nodes = g.nodes()
    removed = np.random.choice(nodes, node_nr)
    g.remove_nodes_from(removed)
    return g


def to_csv(title, L, k_dict):
    print(f"writing {title}")
    with open(title, "w") as f:
        writer = csv.writer(f)
        # fieldnames = ["f_val", "P_f / P_0"]
        # writer.writerow(fieldnames)
        writer.writerows(zip(k_dict.keys(), [k / L for k in k_dict.values()]))





# print(g_first.nodes())
# rand_remove(g_first,2)
# print(g_first.nodes())

# g_new = nx.barabasi_albert_graph()
# g_new = nx.watts_strogatz_graph(n=size, k=k, p=0.01)
# g_new = nx.barabasi_albert_graph(size, k*2)

er = GraphType(k_val=[0.5, 1, 2, 4], name='ER', func=nx.fast_gnp_random_graph)
barabasi = GraphType(k_val=[2, 4], name='BAR', func=nx.barabasi_albert_graph)
ws = GraphType(k_val=[2, 4], name='WS', func=nx.watts_strogatz_graph)
ks = [er, barabasi, ws]
# ks = [er]
p_numb = 100
f_list = np.linspace(0, 1, p_numb + 1)


t_bef = time.time()
L_list = [1,10,20]
size = int(1e3)
third_part_closeness(size, ks, L_list)
t_aft = time.time()
print(t_aft - t_bef)
L_list = np.arange(1,12,5)
size = int(1e4)
second_part(size, ks, [1,5,10])