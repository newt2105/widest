import networkx as nx

# Function to print required path
def printpath(parent, vertex, target, path):
    # global parent
    if (vertex < 0):
        return 
    printpath(parent, parent[vertex], target, path)
    path.append(vertex)
    
    
# Function to return the maximum weight
# in the widest path of the given graph
def widest_path_problem(Graph, src, target):
    ver_list = []
    # To keep track of widest distance
    widest = [-10**9]*(len(Graph)+1)
    
    # To get the path at the end of the algorithm
    parent = [-10**9]*(len(Graph)+1)
 
    container = []
    container.append((0, src))
    
    widest[src] = 10**9
    container = sorted(container)
    
    while (len(container)>0):
        temp = container[-1]
        current_src = temp[1]
        del container[-1]
              
        for neighbor in Graph.neighbors(current_src):

            weight = Graph[current_src][neighbor]['weight']
            weight_u_v = weight
            v = neighbor
            u = current_src

            distance = max(widest[v], min(widest[u], weight_u_v))

            # Relaxation of edge and adding into Priority Queue
            if (distance > widest[v]):
                # Updating bottle-neck distance
                widest[v] = distance

                # To keep track of parent
                parent[v] = current_src

                # Adding the relaxed edge in the priority queue
                container.append((distance, v))
                container = sorted(container)

    path = []
    printpath(parent, target, target, path)

    A = widest[target]
    if A < 0:
        path = None
        A = 0
    return A, path


