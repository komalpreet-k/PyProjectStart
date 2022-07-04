from networkx import path_graph, random_layout
import numpy

G = path_graph(9)
pos = random_layout(G, seed=None) # use (either) global default RNG
pos = random_layout(G, seed=42) # local RNG just for this call
pos = random_layout(G, seed=numpy.random) # use numpy global RNG
random_state = numpy.random.RandomState(42)
pos = random_layout(G, seed=random_state)