import networkx as nx
import pulp as pulp
import os
import random
import time

def PhyGraphGen(
        PhyNodeMinCount, PhyNodeMaxCount, 
        PhyNodeMinCapacity, PhyNodeMaxCapacity, 
        PhyEdgeMinCapacity, PhyEdgeMaxCapacity, 
        PhyEdgeDisconnectedMinRate=0, PhyEdgeDisconnectedMaxRate=0
    ):
    __phy_nodes_count = random.randint(PhyNodeMinCount, PhyNodeMaxCount)

    PHYGraph = nx.DiGraph()

    if PhyEdgeDisconnectedMinRate == PhyEdgeDisconnectedMaxRate:
        __phy_disconnected_rate = PhyEdgeDisconnectedMaxRate
    else:
        __phy_disconnected_rate = random.uniform(PhyEdgeDisconnectedMinRate, PhyEdgeDisconnectedMaxRate)

    for i in range(__phy_nodes_count):
        node_capacity = random.randint(PhyNodeMinCapacity, PhyNodeMaxCapacity)
        PHYGraph.add_node(i, weight=node_capacity)
    for i in PHYGraph.nodes:
        for j in PHYGraph.nodes:
            if (i==j):
                continue
            if (PHYGraph.edges.get((i, j), "#NOTFOUND") != "#NOTFOUND"):
                continue
            edge_capacity = random.randint(PhyEdgeMinCapacity, PhyEdgeMaxCapacity)
            PHYGraph.add_edge(i, j, weight=edge_capacity)
            PHYGraph.add_edge(j, i, weight=edge_capacity)

    for i in range(int(__phy_disconnected_rate*len(PHYGraph.edges))):
        link_to_remove = random.choice(list(PHYGraph.edges))
        PHYGraph.remove_edge(link_to_remove[0], link_to_remove[1])

    return PHYGraph