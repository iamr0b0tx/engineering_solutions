# std lib
import json, time, io

# from thirdparty
import pandas as pd
import numpy as np

# lib code
from utils import *
from hardy_cross import runHardyCrossIteration
from SLAM import runSLAMIteration

FOLDER = 'data/9x9'

def main():
    global NODES

    '''the entry of the program'''

    # read from excel file input
    loops = pd.read_excel(f'{FOLDER}/loops.xlsx', index_col=0).fillna(0).astype(int).values
    diameters = pd.read_excel(f'{FOLDER}/diameter.xlsx', index_col=0)
    lengths = pd.read_excel(f'{FOLDER}/length.xlsx', index_col=0)
    inlets = pd.read_excel(f'{FOLDER}/inlet.xlsx')
    outlets = pd.read_excel(f'{FOLDER}/outlet.xlsx')

    loops_n = loops.max().max()
    all_loops = []
    al_lps = []

    for i in range(1, loops_n+1):
        cols, inds = np.where(loops == i)
        all_loops.append([])
        
        for j, col in enumerate(cols):
            lp = (col+1, inds[j]+1)
            all_loops[-1].append(lp)
            al_lps.append(lp)

    for loop in all_loops:
        pprint(loop, file=FILE)
        
    loops = all_loops.copy()
    all_loops = al_lps.copy()

    # display number of loops
    pprint('\n{} loop(s) found\n=======================\n'.format(loops_n), file=FILE)

    if loops_n == 0:
        pprint('no loop', file=FILE)
        return 0

    length_nans = lengths.isnull()
    diameter_nans = diameters.isnull()

    for current_loop in loops:
        for node1, node2 in current_loop:
            if length_nans[node1][node2]:
                length = lengths[node2][node1]
                lengths[node1][node2] = length
            
            else:
                length = lengths[node1][node2]
                lengths[node2][node1] = length

            if diameter_nans[node1][node2]:
                diameter = diameters[node2][node1]
                diameters[node1][node2] = diameter

            else:
                diameter = diameters[node1][node2]
                diameters[node2][node1] = diameter
            
            # add dummy K
            addK(node1, node2)

            if not inlets[node1].isna().any():
                q_in = inlets[node1][0]
                # pprint('inlet =', q_in, end=', ', file=FILE)
                addLet(q_in, node1, INLET)

            if not outlets[node1].isna().any():
                q_out = outlets[node1][0]
                # pprint('outlet =', q_out, end=', ', file=FILE)
                addLet(q_out, node1, OUTLET)

        #         pprint(file=FILE)
        # pprint(file=FILE)

    # show the nodes
    # pprint(NODES, file=FILE)

    # get all flows
    splitFlow(loops, NODES, diameters, lengths)

    # show the nodes
    for n1 in NODES:
        pprint(n1, '=>', file=FILE)

        for n2 in NODES[n1]:
            pprint('  ', n2, '=>', NODES[n1][n2], file=FILE)
    pprint(file=FILE)

    algorithm = input('Type 0 for Hardy cross OR 1 for simultaneous loop: ')
    valid_input = False
    while not valid_input:
        try:
            input_received = int(algorithm.strip())

            if input_received == 1:
                algorithm = 'Simultaneous Loop'
                valid_input = True

            elif input_received == 0:
                algorithm = 'Hardy Cross'
                valid_input = True

            else:
                valid_input = False

        except:
            algorithm = input(
                'Type 0 for Hardy cross OR 1 for simultaneous loop: '
            )

    # number of iterations
    n_of_iteration = 1000

    # startig time
    start_time = time.time()

    # start iteration
    for i in range(n_of_iteration):
        iteration = i+1
        pprint('iteration {} ->>>>>>>'.format(iteration), file=FILE)

        if input_received == 0:
            correction_factors = runHardyCrossIteration(
                K, N, NODES, Q, QNODE, F, loops, lengths, diameters, iteration
            )

        else:
            correction_factors = runSLAMIteration(
                K, N, NODES, Q, QNODE, F, loops, lengths, diameters, iteration
            )

        if (abs(correction_factors) < 0.0001).all():
            break
    
    output = 'Executed {} iteration(s) of {} in  {:.10f}sec(s)'.format(
        iteration, algorithm, time.time() - start_time
    )
    pprint(output, file=FILE)
    print(output)
    
    if type(FILE) == io.TextIOWrapper:
        FILE.close()

    WRITER.close()
    

def writeJson(filepath, d):
    with open(filepath, 'w') as f:
        json.dump(d, f)


def readJson(filepath):
    with open(filepath) as f:
        return json.load(f)

if __name__ == '__main__':
    collecting_input = 0
    main()
