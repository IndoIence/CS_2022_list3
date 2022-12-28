from dataclasses import dataclass
import networkx as nx
import numpy as np
import csv


def rand_remove(g: nx.classes.graph.Graph, node_nr: int):
    assert node_nr >= 0, "give a positive number of nodes to remove"
    nodes = g.nodes()
    removed = np.random.choice(nodes, node_nr)
    g.remove_nodes_from(removed)
    return g


@dataclass
class GraphType:
    name: str
    k_val: list
    func: any

    def make_new(self, n, param):
        if self.name == 'ER':
            self.func(n=n, p=(param / n))
        elif self.name == 'BAR':
            self.func(n=n, m=2 * param)
        elif self.name == 'WS':
            self.func(n=n, k=param, beta=0.01)
        else:
            raise ValueError("No supported graph type found")


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
f_list = np.linspace(0, 1, p_numb, endpoint=False)
L_list = np.arange(1, 5)
# k = 1 / 500
size = int(1e4)
for L in L_list:
    for gr in ks:
        for k in gr.k_val:
            k_dict = {f: 0 for f in f_list}
            for _ in range(L):
                g_new = er.make_new(size, k)
                giant_before = max(nx.connected_components(g_new), key=len)
                # number of nodes to be removed every iteration
                n = round(1 / p_numb * len(g_new.nodes()))
                for f in f_list:
                    g_after = rand_remove(g_new, n)
                    giant_after = max(nx.connected_components(g_after), key=len)
                    k_dict[f] += len(giant_after) / len(giant_before)

            # title = f"output_old/GC_ws_{k}_{size:.1g}_{L}.csv"
            title = f"output/GC_{gr.name}_{k}_{size:.1g}_{L}.csv"
            print(f"writing {title}")
            with open(title, "w") as f:
                writer = csv.writer(f)
                # fieldnames = ["f_val", "P_f / P_0"]
                # writer.writerow(fieldnames)
                writer.writerows(zip(k_dict.keys(), [k / L for k in k_dict.values()]))
            # k_dict = {}
