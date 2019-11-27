from math import pi
from collections import defaultdict


# key words identifiers
DONE = 'done'  # end input keyword
INLET = '_inlet_'  # the inlet id
OUTLET = '_outlet_'  # the outlet id
K = 'K' #the repr of K
Q = 'Q'  # the repr of Q value
QNODE = 'QNODE'  # the repr of Q value
N = 2
F = 0.024
g = 9.81

# the network
NODES = defaultdict(dict)

def addK(node1, node2, l, d):
    k = (8 * F * l) / ((pi**2) * g * (d**5)) 
    for node in [node1, node2]:
        if node not in NODES:
            NODES[node] = {}

    NODES[node1][node2] = {K: k, Q: 0, QNODE:0}
    NODES[node2][node1] = {K: k, Q: 0, QNODE:0}

def addLet(q, node, KEYWORD):
    q = -q if KEYWORD == OUTLET else q
    NODES[node][KEYWORD] = {K: None, Q: q, QNODE:q}

def done(inp):
    if inp.lower() == DONE:
        return True
    return False

def gettingInlets():
    return getLets('inlet', INLET)

def gettingOutlets():
    return getLets('outlet', OUTLET)

def getLets(prompt, KEYWORD):
    ''' get the nodes and the inlets of the nodes'''
    global NODES

    valid = False
    while not valid:
        # collect the input form user
        inp = input(f'Specify the node and {prompt}[E.g. 1 20]: ')

        # check if user input is done
        if done(inp):
            print(f'==================All {prompt} values loaded!======================\n')
            return False

        # check if the input splits as it should
        inp = inp.split()
        if len(inp) != 2:
            print('Invalid Number of Values Specified!\n')
            continue
        
        # grab the params
        node, q = inp
        
        # if the node is known
        if node not in NODES:
            print('Unknown Node Specified!\n')
            continue
        
        # try to get the q as number
        try:
            q = float(q)

        except:
            print(f'Invalid Value of Q for node {node}!\n')
            continue
        
        valid = True
        addLet(q, node, KEYWORD)
    return True

def gettingK():
    ''' get the nodes and the K of the pipes that connect them'''
    global NODES

    valid = False
    while not valid:
        inp = input('Specify the (node from) and (node to) and (length, diameter) seperated by space[e.g 1 2 50 10]: ')

        if done(inp):
            print('==================All Length and Diameters values loaded!======================\n')
            return False

        inp = inp.split()
        if  len(inp) != 4:
            print('Invalid Number of Values Specified!\n')
            continue
        
        try:
            l, d = list(map(float, inp))

        except:
            print('Invalid Value of length / diameter!\n')
            continue

        valid = True
        addK(node1, node2, l, d)
    return True

def splitFlow(all_loops, NODES):
    for node in NODES:
        inlet, outlet = 0, 0

        n = len(NODES[node])
        if INLET in NODES[node]:
            inlet = NODES[node][INLET][QNODE]
            n -= 1

        if OUTLET in NODES[node]:
            outlet = NODES[node][OUTLET][QNODE]
            n -= 1

        qs = [NODES[node][nodex][QNODE] for nodex in NODES[node]]
        n = qs.count(0)

        if n == 0:
            continue

        q_i = -sum(qs) / n

        for connected_node in NODES[node]:
            if connected_node in [INLET, OUTLET]:
                continue
            
            # print(node, connected_node)
            if (node, connected_node) in all_loops:
                q1, q2 = abs(q_i), -abs(q_i)
                all_loops.remove((node, connected_node))

            if NODES[node][connected_node][Q] == 0:
                NODES[node][connected_node][Q] = q1

            if NODES[connected_node][node][Q] == 0:
                NODES[connected_node][node][Q] = q2

            if NODES[node][connected_node][QNODE] == 0:
                NODES[node][connected_node][QNODE] = q_i

            if NODES[connected_node][node][QNODE] == 0:
                NODES[connected_node][node][QNODE] = -q_i
    return

def updateNodes(cfs, Q, QNODE, NODES):
    def mean(li): return sum(li)/len(li) if len(li) > 0 else 0

    for nn in cfs:
        node1, node2 = nn
        cf = mean(cfs[nn])
    
        NODES[node1][node2][Q] += cf
        NODES[node2][node1][Q] += cf

        NODES[node1][node2][QNODE] += cf
        NODES[node2][node1][QNODE] += cf
    return
