from utils import updateNodes, pprint, FILE

import numpy as np


def runHardyCrossIteration(K, N, NODES, Q, QNODE, F, loops, lengths, diameters, iteration):
    # correction factors
    cfs = {}

    correction_factors = []
    for loop_i, current_loop in enumerate(loops):
        pprint('loop = {}, current_loop = {}'.format(loop_i+1, current_loop), file=FILE)

        s_hl, s = 0, 0
        nodes = []
        for nn in current_loop:
            node1, node2 = nn
            nodes.append(nn)
            
            if nn not in cfs:
                cfs[nn] = []
            
            # the assumed flow rate and k
            q_a = NODES[node1][node2][Q]
            k = NODES[node1][node2][K]
            f = NODES[node1][node2][F]

            # calc for this iteration
            hl = k * (abs(q_a)**N)
            hl = -hl if q_a < 0 else hl
            result = N * abs(hl/q_a)

            # sigma
            s_hl += hl
            s += result

            # qo, hlo, itero = q_a, hl, iter
            # display iter result
            pprint('node: {} to {}, q = {}, k = {}, F = {}, H_L = {}, iter = {}'.format(
                    node1, node2, q_a, k, f, hl, result
                ),
                file=FILE
            )

        # correction factor
        delta = -(s_hl / s)
        
        # relate correction factor to all nodes of this iteration
        for nn in nodes:
            cfs[nn].append(delta)

        pprint(f'delta = {delta}\n', file=FILE)

        correction_factors.append(delta)

    correction_factors = np.array(correction_factors)
    pprint('Correction\n============\n{}\n'.format(
        correction_factors), file=FILE)

    # update the nodes
    updateNodes(cfs, Q, QNODE, NODES, lengths, diameters, iteration)
    return correction_factors
