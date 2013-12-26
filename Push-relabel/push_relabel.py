'''
implement network flow push-relabel algorithm
'''
import networkx as nx
from pprint import pprint
import networkflow


c = 'capacity'
f = 'flow'
h = 'height'

nodes_has_ef = []   # node ef > 0

def InitGraph(edges, st):
    G = nx.DiGraph()
    G.add_edges_from(edges)
    n = len(G.nodes())
    source = st['s']
    target = st['t']
    for id in G.nodes():
        G.node[id][h] = n if id == source else 0
        for toNode in G.successors(id):
            G.edge[id][toNode][f] = G.edge[id][toNode][c] if id == st['s'] else 0
            
    global nodes_has_ef
    nodes_has_ef = [id for id in G.nodes() if id not in {source,target}]
    print(G.nodes(data=True))
    print(G.edges(data=True))
    return G


def Update_ef(G, v, w, st):
    '更新nodes_has_ef, 考察输入的两个结点处是否还有余量'
    for node in (v, w):
        ef = calc_ef(G, node)
        if ef == 0 and node in nodes_has_ef:
            nodes_has_ef.remove(node)
        elif ef > 0 and node not in st.values() and node not in nodes_has_ef:
            nodes_has_ef.append(node)  # s,t不算余量
        elif ef < 0:
            print("Excess < 0!!!")
    

def calc_ef(G, v):
    '计算结点余量'
    flow_in = 0
    flow_out = 0
    pres = G.predecessors_iter(v)
    sucs = G.successors_iter(v)
    flow_in = sum([G.edge[pre][v][f] for pre in pres])
    flow_out = sum([G.edge[v][suc][f] for suc in sucs])
    return flow_in - flow_out
    

def Push(G, Gf, v, w, st): 
    ef_v = calc_ef(G, v)
    if c in Gf[v][w]:   # forward edge has capacity attr in Gf
        edge_attr = G.edge[v][w]
        f_e = edge_attr[f]
        c_e = edge_attr[c]
        delta = min(ef_v, c_e-f_e)
        edge_attr[f] = f_e + delta
    else:
        edge_attr = G.edge[w][v]
        f_e = edge_attr[f]
        delta = min(ef_v, f_e)
        edge_attr[f] = f_e - delta
    Update_ef(G, v, w, st)


def Relabel(G, Gf, v):
    for w in G.nodes():
        if Gf.has_edge(v, w) and G.node[v][h] > G.node[w][h]:break
    else:   # for all edge(v,w) h(v) < h(w), relabel v
        G.node[v][h] += 1
        return True     # return True if do relabel
    return False    
    

def PreflowPush(edges, st):
    G = InitGraph(edges, st)
    Gf = networkflow.GetResidual(G) # update every time fe changes
    n = 1
    while nodes_has_ef:
        v = nodes_has_ef[0]
        flag = 1    # 进行了某项操作, flag置0, 否则使用下一个ef>0的点
        while flag:
            for w in G.nodes():
                if Gf.has_edge(v, w) and G.node[w][h] < G.node[v][h]:
                    Push(G, Gf, v, w, st)
                    Gf = networkflow.GetResidual(G)
                    flag = 0
                    break
            else:
                if Relabel(G, Gf, v):
                    flag = 0
                else:
                    v = nodes_has_ef[nodes_has_ef.index(v)+1] # next node
                
        #networkflow.PlotG(G)
        print('\n第{0}次更新'.format(n))
        n += 1
        pprint(G.nodes(data=True))
        pprint(G.edges(data=True))
        


if __name__ == '__main__':
    edges, st = networkflow.Read('input.txt')
    PreflowPush(edges, st)