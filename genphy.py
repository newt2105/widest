import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt


from gen import PhyGraphGen


random_nodePHY = random.randint(2, 8)

def create_random_physical_network():
   return PhyGraphGen(10,10,10,10,3,10,0.75,0.75)


if __name__=="__main__":
   PHY = create_random_physical_network()
   print(PHY)
   for u,v in PHY.edges:
      print(f"{u}_{v}: ", PHY[u][v]['weight'])
#    nx.draw(PHY)
#    plt.show()
   


