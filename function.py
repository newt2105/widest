import networkx as nx

net = nx.DiGraph()
net.add_node(1, weight=3)
net.add_node(2, weight=8)
net.add_node(3, weight=15)
net.add_node(4, weight=5)
net.add_node(5, weight=5)
net.add_edge(1, 2, weight=7)
net.add_edge(2, 3, weight=8)
net.add_edge(3,4, weight=6)
net.add_edge(4,2, weight=7)
net.add_edge(5,4, weight=4)
net.add_edge(2,5, weight=2)

# Function to print required path
def printpath(parent, vertex, target, path):
    # global parent
    if (vertex == 0):
        return 
    printpath(parent, parent[vertex], target, path)
    
    path.append(vertex)
    
    # print(vertex ,end="\n" if (vertex == target) else "--")
    
    
    
 
# Function to return the maximum weight
# in the widest path of the given graph
def widest_path_problem(Graph, src, target):
    ver_list = []
    # To keep track of widest distance
    widest = [-10**9]*(len(Graph)+1)
    
    # To get the path at the end of the algorithm
    parent = [0]*(len(Graph)+1)
 
    container = []
    container.append((0, src))
    
    widest[src] = 10**9
    container = sorted(container)
    
    while (len(container)>0):
        temp = container[-1]
        current_src = temp[1]
        del container[-1]
  
        
            
        for neighbor in Graph.neighbors(current_src):
            # print("current: ", current_src)
            # print("nei:", neighbor)
            # Lấy trọng số của cạnh
            weight = Graph[current_src][neighbor]['weight']
            weight_u_v = weight
            v = neighbor
            u = current_src
            # print("u:", u)
            # print("v: ", v)
            # print("wei_u_v: ",weight_u_v)
            # print(f"widest {v}:", widest[v], f"_widest {u}:",widest[u])
            distance = max(widest[v], min(widest[u], weight_u_v))
            # print("dis: ",distance)
            # print("--")
    
            
    

            # Relaxation of edge and adding into Priority Queue
            if (distance > widest[v]):
                # Updating bottle-neck distance
                widest[v] = distance
                # print("widest_update: ",widest)
                # To keep track of parent
                parent[v] = current_src
                # print("parent_update: ",parent)
                # Adding the relaxed edge in the priority queue
                container.append((distance, v))
                container = sorted(container)
                # print("container_update: ", container)
                # print("--")
    path = []
    printpath(parent, target, target, path)
    print(path)
    

    # ver_list.append(A)
    return widest[target]

# print(widest_path_problem(net, 4, 1))
