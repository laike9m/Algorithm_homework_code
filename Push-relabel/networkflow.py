'''
c This is a simple example file to demonstrate the DIMACS
c input file format for maximum flow problems. The solution
c vector is [5,10,5,0,5,5,10,5] with cost at 15.
c Problem line (nodes, links)
p max 6 8
c source
n 1 s
c sink
n 6 t
c Arc descriptor lines (from, to, capacity)
a 1 2 5
a 1 3 15
a 2 4 5
a 2 5 5
a 3 4 5
a 3 5 5
a 4 6 15
a 5 6 5
c
c End of file
'''

import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint

c = 'capacity'
f = 'flow'
w = 'weight'


def Read(filename):
    
    edges = []
    st = {}
    
    with open(filename, 'rt') as f:
        for line in f.readlines():
            if line.startswith('a'):
                fromNode, toNode, capacity = line.split()[1:]
                edges.append((fromNode, toNode, {'capacity': int(capacity)}))
            elif line.startswith('n'):
                node, type = line.split()[1:]
                st[type] = node
            
    return edges, st


def PlotG(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(G, pos,)
    plt.show()
    

def GetResidual(G, plot=False):
    'generate residual graph'
    Gf = nx.DiGraph(G)
    for fromNode, toNode in Gf.edges():
        edge_attr = Gf.edge[fromNode][toNode]
        flow = edge_attr[f]
        capacity = edge_attr[c]
        if flow == 0:
            edge_attr[w] = edge_attr[f]
            del edge_attr[f]  # replace key 'flow' with 'weight'
        elif flow < capacity :
            edge_attr[w] = capacity - flow
            del edge_attr[f]   
            Gf.add_edge(toNode, fromNode, attr_dict={w: flow})
        elif flow == capacity:
            Gf.add_edge(toNode, fromNode, attr_dict={w: flow})
            Gf.remove_edge(fromNode, toNode)
        else:
            print('flow is greater than capacity!!!')
            return    
    pprint(Gf.edges(data=True))
    if plot:
        PlotG(G)
    return Gf
            
            
def TestResidual(edges):
    # init
    G = nx.DiGraph()
    G.add_edges_from(edges)
    n = len(G.nodes())
    for v, w in G.edges_iter():
        G.edge[v][w][f] = 0
    G.edge['1']['2'][f] = G.edge['2']['3'][f] = G.edge['3']['4'][f] = 1
    # test
    GetResidual(G, plot=True)


def ModifyResidual():
    pass


if __name__ == '__main__':
    #edges, st = Read('input.txt')
    #print(edges, st)
    edges, _ = Read('input2.txt')
    TestResidual(edges)