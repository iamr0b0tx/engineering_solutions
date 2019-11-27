# std lib
import json, time

# from thirdparty
import pandas as pd
import numpy as np

# lib code
from utils import *
from hardy_cross import runHardyCrossIteration
from SLAM import runSLAMIteration

def main():
    global NODES, collecting_input

    '''the entry of the program'''

    if collecting_input == 1:
        # get the node network
        while gettingK():
            pass

        # the inlet
        while gettingInlets():
            pass

        # the outlet
        while gettingOutlets():
            pass

        writeJson('nodes.json', NODES)

    elif collecting_input == -1:
        NODES = readJson('nodes.json')
    
    else:
        # read from excel file input
        loops = pd.read_excel('loops.xlsx', index_col=0).fillna(0).astype(int).values
        diameters = pd.read_excel('diameter.xlsx', index_col=0)
        lengths = pd.read_excel('length.xlsx', index_col=0)
        inlets = pd.read_excel('inlet.xlsx')
        outlets = pd.read_excel('outlet.xlsx')

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
            print(loop)
            
        loops = all_loops.copy()
        all_loops = al_lps.copy()

        # display number of loops
        print('\n{} loop(s) found\n=======================\n'.format(loops_n))

        if loops_n == 0:
            print('no loop')
            return 0

        length_nans = lengths.isnull()
        diameter_nans = diameters.isnull()
        for current_loop in loops:
            for node1, node2 in current_loop:
                # print(node1, end=', ')

                if length_nans[node1][node2]:
                    length = lengths[node2][node1]
                else:
                    length = lengths[node1][node2]

                if diameter_nans[node1][node2]:
                    diameter = diameters[node2][node1]
                else:
                    diameter = diameters[node1][node2]
                
                addK(node1, node2, length, diameter)

                if not inlets[node1].isna().any():
                    q_in = inlets[node1][0]
                    # print('inlet =', q_in, end=', ')
                    addLet(q_in, node1, INLET)

                if not outlets[node1].isna().any():
                    q_out = outlets[node1][0]
                    # print('outlet =', q_out, end=', ')
                    addLet(q_out, node1, OUTLET)

        #         print()
        # print()

    # show the nodes
    # print(NODES)

    # get all flows
    splitFlow(all_loops, NODES)

    # show the nodes
    for n1 in NODES:
        print(n1, '=>')

        for n2 in NODES[n1]:
            print('  ', n2, '=>', NODES[n1][n2])
    print()

    algorithm = input('Type 0 for Hardy cross OR 1 for simultaneous loop: ')
    valid_input = False
    while not valid_input:
        try:
            input_received = int(algorithm.strip())

            if input_received == 1:
                algorithm = 'Simultaneous Loop'
            
            elif input_received == 0:
                algorithm = 'Hardy Cross'

            else:
                valid_input = False

            valid_input = True
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
        print('iteration {} ->>>>>>>'.format(i+1))

        if input_received == 1:
            diff = runHardyCrossIteration(K, N, NODES, Q, QNODE, loops)

        else:
            diff = runSLAMIteration(K, N, NODES, Q, QNODE, loops)

        if abs(diff) < 0.01:
            break
    
    print('Executed {} in  {:.10f}sec(s)'.format(algorithm, time.time() - start_time))

def writeJson(filepath, d):
    with open(filepath, 'w') as f:
        json.dump(d, f)


def readJson(filepath):
    with open(filepath) as f:
        return json.load(f)


if __name__ == '__main__':
    collecting_input = 0
    main()
