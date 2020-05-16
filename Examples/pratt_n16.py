import os
import sys
sys.path.append(os.getcwd())

import numpy as np
import TrussSolver as ts 

c = 250
side = 190/3
height = 50
h1 = 50
h2 = height - h1
h3 = 0
l1 = side
l2 = side
l3 = side


L = [l1, l1+l2, 190, c]
H = [h1, h1 + h2, height , height]



nodes = np.array([    
    [0,0],          #0
    [L[0],0],       #1
    [L[1],0],       #2
    [L[2],0],       #3
    [L[3],0],       #4
    [2*c - L[2],0], #5
    [2*c - L[1],0], #6
    [2*c - L[0],0], #7
    [2*c       ,0], #8

    [L[0],H[0]],    #9
    [L[1],H[1]],    #10
    [L[2],H[2]],    #11
    [L[3],H[3]],    #12
    [2*c - L[2],H[2]],#13
    [2*c - L[1],H[1]], #14
    [2*c - L[0],H[0]]#15

    ])

connections = np.array([
    [1,9],              #0
    [0,9,2],            #1
    [1,9,10,3],         #2
    [2,10,11,4],        #3
    [3,11,12,13,5],     #4
    [4,13,14,6],        #5
    [5,14,15,7],        #6
    [6,15,8],           #7
    [7,15],             #8

    [0,1,2,10],         #9
    [9,2,3,11],         #10
    [10,3,4,12],         #11
    [11,4,13],          #12
    [12,4,5,14],        #13
    [13,5,6,15],         #14
    [14,6,7,8]          #15

    ])

t1 = ts.Truss(nodes,connections)

load = 1

t1.addLoad(0,[0,load/2])
t1.addLoad(8,[0,load/2])
t1.addLoad(11,[0,-load/3])
t1.addLoad(12,[0,-load/3])
t1.addLoad(13,[0,-load/3])


t1.solve()

print("\nNodes:\t\t", len(nodes))
print("Weight:\t\t", round(t1.truss_weight(),2))
print("Fmax Tension:\t", round(t1.fmax_tension,2))
print("LTW (tension):\t", round(t1.ltw_tension,3))
print()





trussdraw = ts.PgTruss(t1,1600)
trussdraw.drawNodes()
