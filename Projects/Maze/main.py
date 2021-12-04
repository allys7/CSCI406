import matplotlib.pyplot as plt
import networkx as nx
import read_inputs as ri

grid = ri.read_file_to_2dlist("input.txt")
forward, backward = ri.generate_graph_from_grid(grid)

# shift backwards graph to the right
pos_back = nx.spring_layout(backward)
for k,v in pos_back.items():
    # Shift the x values of every node by 20 to the right
    v[0] = v[0] + 3


nx.draw(forward, with_labels=True, font_weight='bold')
nx.draw(backward, pos_back, with_labels=True, font_weight='bold')
plt.show()