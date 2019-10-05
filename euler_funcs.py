import networkx as nx
import matplotlib.pyplot as plt
import operator

# generate a random directed graph

def show_node_path(eulerized):
    # get eulerian order
    edges = nx.eulerian_circuit(eulerized)
    edges = list(edges)
    new_graph = nx.DiGraph()
    for i in range(len(edges)):
        new_graph.add_edge(edges[i][0], edges[i][1], weight = i)
    edges_labels = dict([((u,v), d['weight']) for u,v,d in new_graph.edges(data=True)])
    sorted_labels = sorted(edges_labels.items(), key = operator.itemgetter(1))
    
    print(sorted_labels)
    return sorted_labels

def create_erdos_renyi(num_nodes):
    # randomly generate the nodes and edge probability
#     rand_num_nodes = random.randint(1, rand_max)
#     rand_prob = random.random()
    # create a random erdos renyi graph
    non_directed_graph = nx.erdos_renyi_graph(num_nodes, 0.9)
    
    count = 0
    while count < 50 or not nx.is_eulerian(non_directed_graph):
        non_directed_graph = nx.erdos_renyi_graph(num_nodes, 0.9)
        count += 1
    if nx.is_eulerian(non_directed_graph):
        # create directed version of barabasi albert
        eulerized = nx.eulerize(non_directed_graph)
        di_euler_graph = nx.DiGraph()
        di_euler_graph.add_nodes_from(eulerized)
        di_euler_graph.add_edges_from(nx.eulerian_circuit(eulerized))
        color_map = ['green' if node == 0 else 'red' for node in di_euler_graph]
        sorted_labels = show_node_path(eulerized)
        
        labeldict = {}
        for i in di_euler_graph.nodes:
            lst = []
            for j in range(len(sorted_labels)):
                if sorted_labels[j][0][0] == i:
                    lst.append(sorted_labels[j][1])
            labeldict[i] = str(lst).strip('[]')
        
        nx.draw(di_euler_graph, node_color = color_map, labels=labeldict, with_labels=True, font_weight='bold')
        print("Is Eulerian?: " + str(nx.is_eulerian(di_euler_graph)))
        
        
        
    else: # if not eulerian print not eulerian
        print("Is Eulerian?: " + str(nx.is_eulerian(non_directed_graph)))
    
def create_watts_strogatz_graph(num_nodes):
    # randomly generate the nodes and edge probability
#     rand_num_nodes = random.randint(3, rand_max)
#     rand_neighbors = 0
#     if rand_num_nodes > 3:
#         rand_neighbors = random.randint(2, rand_num_nodes-1)
#     else:
#         rand_neighbors = 2
#     rand_prob = random.random()
    # create a random erdos renyi graph
    non_directed_graph = nx.watts_strogatz_graph(num_nodes, num_nodes-1, 0.9)
    
    count = 0
    while count < 50 or not nx.is_eulerian(non_directed_graph):
        non_directed_graph = nx.watts_strogatz_graph(num_nodes, num_nodes-1, 0.9)
        count += 1
    if nx.is_eulerian(non_directed_graph):
        # create directed version of barabasi albert
        eulerized = nx.eulerize(non_directed_graph)
        di_euler_graph = nx.DiGraph()
        di_euler_graph.add_nodes_from(eulerized)
        di_euler_graph.add_edges_from(nx.eulerian_circuit(eulerized))
        color_map = ['green' if node == 0 else 'red' for node in di_euler_graph]
        sorted_labels = show_node_path(eulerized)
        
        labeldict = {}
        for i in di_euler_graph.nodes:
            lst = []
            for j in range(len(sorted_labels)):
                if sorted_labels[j][0][0] == i:
                    lst.append(sorted_labels[j][1])
            labeldict[i] = str(lst).strip('[]')
        
        nx.draw(di_euler_graph, node_color = color_map, labels=labeldict, with_labels=True, font_weight='bold')
        print("Is Eulerian?: " + str(nx.is_eulerian(di_euler_graph)))
    else:
        print("Is Eulerian?: " + str(nx.is_eulerian(non_directed_graph)))
