import pandas as pd
import numpy as np

from collections import defaultdict
from utils import updateNodes, pprint, FILE

def runSLAMIteration(K, N, NODES, Q, QNODE, F, loops, lengths, diameters, iteration):
    # the loops
    loops_n = len(loops)

    J = pd.DataFrame(data=0.0, index=range(loops_n), columns=range(loops_n))
    R = pd.DataFrame(data=0.0, index=range(loops_n), columns=[0])[0]
    
    loop_pipes = []
    for i, loop_a in enumerate(loops):
        loop_pipes.append(loop_a)

        pprint(loop_a, file=FILE)
        for j, loop_b in enumerate(loops):
            # the common pipe
            intersect = [pipe for pipe in loop_a if pipe in loop_b or pipe[::-1] in loop_b]

            pprint('  ', loop_a, intersect, file=FILE)

            for node1, node2 in intersect:
                k, q = NODES[node1][node2][K], NODES[node1][node2][Q]
                f = NODES[node1][node2][F]
                
                # head loss
                hl = k * (abs(q)**N)
                
                J[i][j] += N * hl / abs(q)

                if q < 0:
                    hl *= -1

                if i == j:
                    R[i] += hl

                pprint('      n {} to {}, k = {}, q = {}, F = {}, hl = {}, nhl/q = {}'.format(
                    node1, node2, k, q, f, hl, N * hl / abs(q)),
                    file=FILE
                )
                
            if i != j:
                J[i][j] = -J[i][j]
            
        R[i] = -R[i]
        pprint(file=FILE)
            
    J_inv = pd.DataFrame(np.linalg.pinv(J.values), J.columns, J.index)
    correction_factors = J_inv.dot(R)

    pprint('Jacobian\n============\n{}\n'.format(J), file=FILE)
    pprint('RHS\n============\n{}\n'.format(R), file=FILE)
    pprint('Correction\n============\n{}\n'.format(correction_factors), file=FILE)
    # input()

    cfs = defaultdict(list)
    for i in range(loops_n):
        for pipe in loop_pipes[i]:
            cfs[pipe].append(correction_factors[i])

    # update the nodes
    updateNodes(cfs, Q, QNODE, NODES, lengths, diameters, iteration)

    return correction_factors
