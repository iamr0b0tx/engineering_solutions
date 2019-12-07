import sys
from math import pi, log10
from collections import defaultdict

import pandas as pd

# key words identifiers
DONE = 'done'  # end input keyword
INLET = '_inlet_'  # the inlet id
OUTLET = '_outlet_'  # the outlet id
K = 'K'  # the repr of K
Q = 'Q'  # the repr of Q value
QNODE = 'QNODE'  # the repr of Q value
F = 'F'
N = 2
g = 9.81
KINEMATIC_VISCOSITY = 8.9 * (10**-7)
PIPE_ROUGHNESS = 0.0005

WRITER = pd.ExcelWriter('results.xlsx')

# the network
NODES = defaultdict(dict)

log_state = -1

if log_state:
    pprint = print
    FILE = sys.stdout if log_state == 1 else open('results.txt', 'w')

else:
    def pprint(*args, **kwargs):
        pass


def getF(q, d):
    def getF1():
        return 64 / R

    def getF2():
        a = 5.02 * log10(R / (4.518*log10(R / 7)))
        b = R * (1 + ((R**0.52) / (29 * ((d / PIPE_ROUGHNESS)**0.7))))
        root_sf_inv = -2 * log10((a/b) + (1 / (3.7 * d / PIPE_ROUGHNESS)))
        root_sf_inv = -2 * log10(
            (PIPE_ROUGHNESS / (d * 3.7)) + (2.5 * root_sf_inv / R)
        )

        return root_sf_inv ** -2

    # get reynolds number
    R = (4 * q * d) / (pi * (d**2) * KINEMATIC_VISCOSITY)

    if R < 2000:
        return getF1()

    elif R > 4000:
        return getF2()

    else:
        a = getF1()
        c = getF2()

        return c - ((4000 - R) * (c - a) / 2000)


def getK(q, l, d):
    f = getF(q, d)
    return (8 * f * l) / ((pi**2) * g * (d**5)), f

def report(iteration, NODES):
    data = defaultdict(list)
    for n1 in NODES:
        for n2 in NODES[n1]:
            data['Nodal Points'].append(n1)
            data['Connected Members'].append(n2)
            data['K'].append(NODES[n1][n2][K])
            data['Q'].append(NODES[n1][n2][Q])
            data['Q Node'].append(NODES[n1][n2][QNODE])
            data['F'].append(NODES[n1][n2][F])

    pd.DataFrame(data).to_excel(WRITER, sheet_name=f"iteration {iteration}")

def addK(node1, node2, q=1, l=1, d=1):
    k, f = getK(q, l, d)
    for node in [node1, node2]:
        if node not in NODES:
            NODES[node] = {}

    NODES[node1][node2] = {K: k, Q: 0, QNODE: 0, F: f}
    NODES[node2][node1] = {K: k, Q: 0, QNODE: 0, F: f}


def addLet(q, node, KEYWORD):
    q = -q if KEYWORD == OUTLET else q
    NODES[node][KEYWORD] = {K: None, Q: -q, QNODE: q, F: None}


def splitFlow(loops, NODES, diameters, lengths):
    for loop in loops:
        for node, _ in loop:
            qs = [NODES[node][nodex][QNODE] for nodex in NODES[node]]
            n = qs.count(0)

            if n == 0:
                continue

            # get the q that is left
            q_i = -sum(qs) / n

            for connected_node in NODES[node]:
                if connected_node in [INLET, OUTLET]:
                    continue

                # update the k value
                k, f = getK(
                    abs(q_i),
                    lengths[node][connected_node],
                    diameters[node][connected_node]
                )

                if NODES[node][connected_node][Q] == 0:
                    NODES[node][connected_node][Q] = -q_i
                    NODES[node][connected_node][QNODE] = q_i
                    NODES[node][connected_node][K] = k
                    NODES[node][connected_node][F] = f

                if NODES[connected_node][node][Q] == 0:
                    NODES[connected_node][node][Q] = q_i
                    NODES[connected_node][node][QNODE] = -q_i
                    NODES[connected_node][node][F] = f
                    NODES[connected_node][node][K] = k
    
    report(0, NODES)
    return


def updateNodes(cfs, Q, QNODE, NODES, lengths, diameters, iteration):
    def mean(li): return sum(li)/len(li) if len(li) > 0 else 0

    for nn in cfs:
        node1, node2 = nn
        cf = mean(cfs[nn])

        # get the q respective to the loop direction
        NODES[node1][node2][Q] += cf
        NODES[node2][node1][Q] = -NODES[node1][node2][Q]

        # update the q respective to the node
        NODES[node1][node2][QNODE] = (
            NODES[node1][node2][QNODE] / abs(NODES[node1][node2][QNODE])
        ) * NODES[node1][node2][Q]

        NODES[node2][node1][QNODE] = (
            NODES[node2][node1][QNODE] / abs(NODES[node2][node1][QNODE])
        ) * NODES[node2][node1][Q]

        # update the k value
        k, f = getK(
            abs(NODES[node1][node2][Q]),
            lengths[node1][node2],
            diameters[node1][node2]
        )

        NODES[node1][node2][K] = k
        NODES[node1][node2][F] = f

        NODES[node2][node1][K] = k
        NODES[node2][node1][F] = f

    report(iteration, NODES)

    return
