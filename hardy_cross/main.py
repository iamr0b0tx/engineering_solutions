from node_creator import *
from networkx.readwrite import json_graph

import json

def getNodePairs(loop):
    for i in range(len(loop) - 1):
        yield loop[i:i+2]

def updateNodes(cfs):
    mean = lambda li:sum(li)/len(li) if len(li) > 0 else 0

    for nn in cfs:
        node1, node2 = nn
        cf = mean(cfs[nn])

        NODES[node1][node2][Q] += cf
        NODES[node2][node1][Q] += cf
    return

def runIteration():
    # the loops
    loops = nx.cycle_basis(G)
    loops_n = len(loops)

    # correction factors
    cfs = {}

    # display number of loops
    print('{} loop(s) found\n=======================\n'.format(loops_n))

    if loops_n == 0:
        input('no loop')
        return

    s_delta = 0
    for loop_i, loop in enumerate(loops):
        current_loop = loop + [loop[0]]
        print('loop = {}, current_loop = {}'.format(loop_i+1, current_loop))
        
        s_hl, s = 0, 0
        nodes = []
        for node1, node2 in getNodePairs(current_loop):
            nn = tuple([node1, node2])
            nodes.append(nn)
            if nn not in cfs:
                cfs[nn] = []


            # the assumed flow rate and k
            q_a = NODES[node2][node1][Q]
            k = NODES[node2][node1][K]

            # calc for this iteration
            hl = k * (abs(q_a)**N)
            hl = -hl if q_a < 0 else hl
            result = N * abs(hl/q_a)

            # sigma
            s_hl += hl;s += result

            # qo, hlo, itero = q_a, hl, iter
            # display iter result
            print('node: {} to {}, q = {}, k = {}, H_L = {}, iter = {}'.format(node1, node2, q_a, k, hl, result))
        
        # correction factor
        delta = -(s_hl / s)

        # relate correction factor to all nodes of this iteration
        for nn in nodes:
            cfs[nn].append(delta)
        
        print(f'delta = {delta}\n')

        s_delta += abs(delta)

    # update the nodes
    updateNodes(cfs)
    return s_delta/loops_n

def splitFlow():
    for node in NODES:
        inlet, outlet = 0, 0
        
        n = len(NODES[node])
        if INLET in NODES[node]:
            inlet = NODES[node][INLET][Q]
            n -= 1
        
        if OUTLET in NODES[node]:
            outlet = NODES[node][OUTLET][Q]
            n -= 1
        
        qs = [NODES[node][nodex][Q] for nodex in NODES[node]]
        n = qs.count(0)

        if n == 0:
            continue

        q_i = -sum(qs) / n

        for connected_node in NODES[node]:
            if connected_node in [INLET, OUTLET]:
                continue
            
            if NODES[node][connected_node][Q] == 0:
                NODES[node][connected_node][Q] = q_i
            
            if NODES[connected_node][node][Q] == 0:
                NODES[connected_node][node][Q] = -q_i
    return

def main():
    global G, NODES

    '''the entry of the program'''

    # # get the node network
    # while gettingK():
    #     pass

    # # the inlet
    # while gettingInlets():
    #     pass

    # # the outlet
    # while gettingOutlets():
    #     pass

    # data = json_graph.node_link_data(G)
    # writeJson('graph.json', data)
    # writeJson('nodes.json', NODES)
    
    G = json_graph.node_link_graph(readJson('graph.json'))
    NODES = readJson('nodes.json')

    # show the nodes
    # print(NODES)

    # get all flows
    splitFlow()

    # show the nodes
    # print(NODES)

    # number of iterations
    n_of_iteration = 1000

    # start iteration
    for i in range(n_of_iteration):
        print('iteration {} ->>>>>>>'.format(i+1))
        diff = runIteration()
        print(diff)
        if abs(diff) < 0.0000001:
            break

    # nx.draw(G, with_labels=True, font_weight='bold')
    # plt.show()


def writeJson(filepath, d):
    with open(filepath, 'w') as f:
        json.dump(d, f)

def readJson(filepath):
    with open(filepath) as f:
        return json.load(f)

if __name__ == '__main__':
    main()
