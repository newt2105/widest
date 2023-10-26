import networkx as nx
from matplotlib import pyplot as plt
from function import widest_path_problem
from genphy import create_random_physical_network



A = create_random_physical_network()
for u,v in A.edges:
   print(f"{u}_{v}: ", A[u][v]['weight'])

# pos = nx.spring_layout(net)
# nx.draw(net,pos, with_labels = True, node_size = 700)
# edge_labels = {(u,v): d['weight'] for u,v,d in net.edges(data= True)}
# nx.draw_networkx_edge_labels(net, pos, edge_labels = edge_labels)
# plt.show()

print(widest_path_problem(A, 1, 3))