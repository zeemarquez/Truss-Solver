import os
import sys
sys.path.append(os.getcwd())

import numpy as np
import TrussSolver as ts 

class Result:
    def __init__(self,truss_,ltw_, h1_, h2_, height_):
        self.truss = truss_
        self.ltw = ltw_
        self.h1 = h1_
        self.h2 = h2_
        self.height = height_

results_list = []
ltw_list = []

for height in range(45,50,5):
    for h1 in range(5,50):

        #h1 = 30

        c = 250
        side = c/3
        #height = 50
        h2 = height-h1
        l1 = 95
        l2 = 95


        L = [l1, l1+l2, c]
        H = [h1, h1 + h2, height ]



        nodes = np.array([    
            [0,0],          #0
            [L[0],0],       #1
            [L[1],0],       #2
            [L[2],0],       #3
            [2*c - L[1],0],   #4
            [2*c - L[0],0],   #5
            [2*c       ,0],   #6
            [L[0],H[0]],    #7
            [L[1],H[1]],    #8
            [L[2],H[2]],    #9
            [2*c - L[1],H[1]],#10
            [2*c - L[0],H[0]] #11

            ])

        connections = np.array([
            [1,7],              #0
            [0,7,2],            #1
            [1,7,8,3],          #2
            [2,8,9,10,4],       #3
            [3,10,11,5],        #4
            [4,11,6],           #5
            [5,11],             #6
            [0,1,2,8],          #7
            [7,2,3,9],          #8
            [8,3,10],           #9
            [9,3,4,11],         #10
            [10,4,5,6]          #11
            ])

        t1 = ts.Truss(nodes,connections)


        t1.addLoad(0,[0,0.6])
        t1.addLoad(6,[0,0.6])
        t1.addLoad(8,[0,-0.4])
        t1.addLoad(9,[0,-0.4])
        t1.addLoad(10,[0,-0.4])



        t1.solve()

        w = t1.truss_weight
        fmax = t1.fmax
        ltw = 1/(fmax*w)

        '''
        print("Weight:", w)
        print("F max:", fmax)
        print("LTW:", ltw)
        '''

        results_list.append(Result(t1,ltw,h1,h2,height))
        ltw_list.append(ltw)



opt_indx = ltw_list.index(max(ltw_list))
opt_result = results_list[opt_indx]
opt_truss = opt_result.truss

w = round(opt_truss.truss_weight(0.0001),3)
fmax = round(opt_truss.fmax,3)
ltw = round(1/(fmax*w),3)

print("\nWeight:\t", w)
print("F max:\t", fmax)
print("LTW:\t", ltw)
print("h1:\t", opt_result.h1)
print("h2:\t", opt_result.h2)
print("Height:\t", opt_result.height)
print()

trussdraw = ts.PgTruss(opt_truss,1600)
trussdraw.drawNodes()

