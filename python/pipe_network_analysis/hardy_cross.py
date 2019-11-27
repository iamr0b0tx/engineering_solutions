from utils import updateNodes

def runHardyCrossIteration(K, N, NODES, Q, QNODE, loops):
    # the loops
    loops_n = len(loops)

    # correction factors
    cfs = {}

    s_delta = 0
    for loop_i, current_loop in enumerate(loops):
        print('loop = {}, current_loop = {}'.format(loop_i+1, current_loop))

        s_hl, s = 0, 0
        nodes = []
        for nn in current_loop:
            node1, node2 = nn

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
            s_hl += hl
            s += result

            # qo, hlo, itero = q_a, hl, iter
            # display iter result
            print('node: {} to {}, q = {}, k = {}, H_L = {}, iter = {}'.format(
                node1, node2, q_a, k, hl, result))

        # correction factor
        delta = -(s_hl / s)
        
        # relate correction factor to all nodes of this iteration
        for nn in nodes:
            cfs[nn].append(delta)

        print(f'delta = {delta}\n')

        s_delta += abs(delta)

    # update the nodes
    updateNodes(cfs, Q, QNODE, NODES)
    return s_delta/loops_n
