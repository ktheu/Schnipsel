# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, labels=None, graph_layout='shell',
               node_size=900, node_color='blue', node_alpha=0.2,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.7,
               text_font='sans-serif'):

    G=nx.DiGraph()

    for edge in graph:
        G.add_edge(edge[0], edge[1])

    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    elif graph_layout == 'circular':
        graph_pos=nx.circular_layout(G)
    else:
        graph_pos=nx.shell_layout(G,scale=2.0)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size,
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels,
                                 label_pos=edge_text_pos)

    plt.axis('off')
    plt.show()

G = {
'a': {'b':3, 'd':9},
'b': {'c':2},
'c': {},
'd': {'a':8,'b':4,'c':5},
}

graph = [(v,w) for v in G for w in G[v]]
labels = [G[v][w] for v in G for w in G[v]]

draw_graph(graph,labels)

#%%
import networkx as nx
import matplotlib.pyplot as plt

inf = float('inf')

G = [[0, 0, 1, 1, 1, 0],  
     [0, 0, 1, 0, 1, 1],  
     [1, 1, 0, 0, 1, 1], 
     [1, 0, 0, 0, 0, 1],  
     [1, 1, 1, 0, 0, 0],  
     [0, 1, 1, 1, 0, 0]]    

nodes = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}

nodlist = list('abcdef')
G0 = nx.Graph()
for v in range(len(G)):
    for w in range(v+1,len(G)):
        if (G[v][w]):
            G0.add_edge(chr(v+97),chr(w+97))

nx.draw_circular(G0,with_labels=True,node_color='y',node_size=600)
plt.show() 

#%%
import networkx as nx
import matplotlib.pyplot as plt

inf = float('inf')

M = [[0, 0, 0, 1, 0, 0],  
     [0, 0, 1, 0, 1, 0],  
     [0, 1, 0, 0, 0, 0], 
     [1, 0, 0, 0, 0, 0],  
     [0, 1, 0, 0, 0, 1],  
     [0, 0, 0, 0, 1, 0]]    

nodlist = list('abcdef')
G = nx.Graph()
for v in range(len(M)):
    for w in range(v+1,len(M)):
        if (M[v][w]):
            G.add_edge(chr(v+97),chr(w+97))

nx.draw_circular(G,with_labels=True,node_color='y',node_size=600)
plt.show()    