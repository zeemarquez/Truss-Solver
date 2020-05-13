import numpy as np
import TrussSolver as ts 

c = 250
side = c/3
height = 50
h1 = 50
h2 = 0
l1 = 83
l2 = 83


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


t1.addLoad(0,[0,0.5])
t1.addLoad(6,[0,0.5])
t1.addLoad(9,[0,-1])


print("\n",t1.bars)
print("\n",t1.nodes[6])

t1.solve()

print("\nWeight: ", t1.truss_weight(1))





'''
trussdraw = ts.PgTruss(t1,1600)
trussdraw.drawNodes()
'''