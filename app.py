import itertools
import copy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_nodes_from([
    (1, {"color": "red"}),
    (2, {"color": "red"}),
    (3, {"color": "red"}),
    (4, {"color": "red"}),
    (5, {"color": "red"}),
    (6, {"color": "red"}),
    (7, {"color": "red"})
])
G.add_edges_from([(1, 2), (1, 7), (7, 6), (6, 2), (6, 5), (2, 3), (2, 5), (5, 3), (3, 4)])

plt.subplot(121)

nx.draw(G, with_labels=True, font_weight='bold')



plt.show()