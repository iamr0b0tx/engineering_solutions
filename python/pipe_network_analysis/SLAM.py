import pandas as pd
import numpy as np

from collections import defaultdict
from utils import updateNodes

def runSLAMIteration(K, N, NODES, Q, QNODE, loops):
    # the loops
    loops_n = len(loops)

    J = pd.DataFrame(data=0.0, index=range(loops_n), columns=range(loops_n))
    R = pd.DataFrame(data=0.0, index=range(loops_n), columns=[0])[0]
    
    loop_pipes = []
    for i, loop_a in enumerate(loops):
        loop_pipes.append(loop_a)

        print(loop_a)
        for j, loop_b in enumerate(loops):
            # the common pipe
            intersect = [pipe for pipe in loop_a if pipe in loop_b or pipe[::-1] in loop_b]

            print('  ', loop_a, intersect)

            for node1, node2 in intersect:
                k, q = NODES[node1][node2][K], NODES[node1][node2][Q]                
                
                # head loss
                hl = k * (abs(q)**N)
                
                J[i][j] += N * hl / abs(q)

                if q < 0:
                    hl *= -1

                if i == j:
                    R[i] += hl

                print('      n {} to {}, k = {}, q = {}, hl = {}, nhl/q = {}'.format(
                    node1, node2, k, q, hl, N * hl / abs(q))
                )
                
            if i != j:
                J[i][j] = -J[i][j]
            
        R[i] = -R[i]
        print()
            
    J_inv = pd.DataFrame(np.linalg.pinv(J.values), J.columns, J.index)
    delta_q = J_inv.dot(R)

    print('Jacobian\n============\n{}\n'.format(J))
    print('RHS\n============\n{}\n'.format(R))
    print('Correction factor\n============\n{}\n'.format(delta_q))
    # input()

    cfs = defaultdict(list)
    for i in range(loops_n):
        for pipe in loop_pipes[i]:
            cfs[pipe].append(delta_q[i])

    # update the nodes
    updateNodes(cfs, Q, QNODE, NODES)

    return delta_q.mean()
