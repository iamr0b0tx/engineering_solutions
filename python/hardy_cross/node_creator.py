import networkx as nx
import matplotlib.pyplot as plt

# the graph
G = nx.Graph()
# G = nx.DiGraph()

# key words identifiers
DONE = 'done'  # end input keyword
INLET = '_inlet_'  # the inlet id
OUTLET = '_outlet_'  # the outlet id
K = 'K' #the repr of K
Q = 'Q' #the repr of Q value
N = 1.85 

# the network
NODES = {}

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
        q = -q if KEYWORD == OUTLET else q
        NODES[node][KEYWORD] = {K: None, Q: q}
        a, b = (f'{KEYWORD}{node}', node) if KEYWORD == INLET else (node, f'{KEYWORD}{node}')
        G.add_edge(a, b, weight=4)
    return True

def gettingK():
    ''' get the nodes and the K of the pipes that connect them'''
    global NODES

    valid = False
    while not valid:
        inp = input('Specify the (node from) and (node to) and (K) seperated by space[e.g 1 2 360]: ')

        if done(inp):
            print('==================All K values loaded!======================\n')
            return False

        inp = inp.split()
        if  len(inp) not in [3, 5]:
            print('Invalid Number of Values Specified!\n')
            continue
        
        if len(inp) == 3:
            node1, node2, k = inp

        else:
            node1, node2, l, D, C = inp
            try:
                l, D, C = float(l), float(D), float(C)

            except:
                print('Invalid Value of K!\n')
                continue
            
            D /= 12
            k = (4.73 * l) / ((C**4.87) * (D**N))

        try:
            k = float(k)

        except:
            print('Invalid Value of K!\n')
            continue
        
        valid = True
        for node in [node1, node2]:
            if node not in NODES:
                NODES[node] = {}

        NODES[node1][node2] = {K: k, Q: 0}
        NODES[node2][node1] = {K: k, Q: 0}
        G.add_edge(node1, node2, weight=4)
    return True
