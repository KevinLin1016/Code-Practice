
#Common Algorithms
import numpy as np
from collections import deque,defaultdict
from copy import copy,deepcopy
import math
#%%
'''
2.Tresure Island I --DEQUE
A map [['O','O','O','O'],
['D','O','D','O'],
['O','O','O','O'],
['D','D','D','O']
]
Treasure island is 'X', 'O' is safe zone, 'D' is dangerous area.
Find the shortest path from top-left position to treasure island.
'''
def find_island(m,s):
    nrow=len(m)
    ncol=len(m[0])

    if nrow<=0 or ncol==0:
        return -1
    
    route=deque([((s[0],s[1]),0)])#route and step
    m[s[0]][s[1]]='D'


    while route:
        (x,y),step=route.popleft()# drop from left side
        
        
        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:#define the movement
            if 0<=x+dx<nrow and 0<=y+dy<ncol:
                if m[x+dx][y+dy]=='X':
                    route.append(((x+dx,y+dy),step+1))#append to right
                    
                    return route[-1][-1]
                if m[x+dx][y+dy]=='O':
                    m[x+dx][y+dy]='D'
                    
                    route.append(((x+dx,y+dy),step+1))
    return -1
    
'''
3.Treasure Island ii
Must start from one of the starting point 'S', find minimum number of steps to treasure island.
[['S','O''O','S','S'],
['D','O','D','O','D'],
['O','O','O','O','X'],
['X','D','D','O','O'],
['X','D','D','D','O']]
'''
def find_island2(m):
    nrow=len(m)
    ncol=len(m[0])
    
    if nrow<=0 or ncol==0:
        return -1   
    
    start=[]
    des=[]
    dis=[]
    
    for i in range(nrow):
        for j in range(ncol):
            if m[i][j]=='S':
                start.append((i,j))
            elif m[i][j]=='X':
                des.append((i,j))
        

    for s in start:
        for d in des:
            dis.append(path(m,s,d))

    print(dis)
    return min(dis)

def path(m,s,d):
        imap=deepcopy(m)#这个很重要，deepcopy原矩阵，否则会改变原矩阵
        nrow=len(imap)
        ncol=len(imap[0])
        route=deque([((s[0],s[1]),0)])#route and step
        imap[s[0]][s[1]]='D'
    
        print(s,d)
        while route:
            (x,y),step=route.popleft()# drop from left side
            
            
            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:#define the movement
                if 0<=x+dx<nrow and 0<=y+dy<ncol:
                    if x+dx==d[0] and y+dy==d[1]:
                        route.append(((x+dx,y+dy),step+1))#append to right
                        
                        return route[-1][-1]
                    if imap[x+dx][y+dy]=='O':
                        imap[x+dx][y+dy]='D'
                        
                        route.append(((x+dx,y+dy),step+1))
        return float('inf')             
                        

'''
4. Knearst Post Offices
Find the k post offices located closet to you.
input you:[0,0] post offices:[[-16,5],[-1,2],[4,3],[10,-2],[0,3],[-5,-9]]
k=3
'''
def knearst_po(y,p,k):
    dis=np.array([])
    location=[]
    for i in p:
        dis=np.append(dis,math.sqrt((i[0]-y[0])**2+(i[1]-y[1])**2))
       
    for j in range(k):
        location.append(np.argmin(dis))#find the index of the minimum value
        dis[np.argmin(dis)]=float('inf')#visted
    
    p=np.array(p)
    return p[location]

'''
5.Roll Dice
A six-sided die is a small cube with a different number of pips on each face (side), ranging from 1 to 6.
On any two opposite side of the cube, the number of pips adds up to 7; that is, there are three pairs of opposite sides: 1 and 6, 2 and 5, and 3 and 4.
There are N dice lying on a table, each showing the pips on its top face. In one move, you can take one die and rotate it to an adjacent face.
For example, you can rotate a die that shows 1 s that it shows 2, 3, 4 or 5. However, it cannot show 6 in a single move, because the faces with one pip and six pips visible are opposite sides rather than adjacent.
You want to show the same number of pips on the top face of all N dice. Given that each of the dice can be moved multiple times, count the minimum number of moves needed to get equal faces.

Write a function that, given an array A consisting of N integers describing the number of pips (from 1 to 6) shown on each die's top face, returns the minimum number of moves necessary for each die show the same number of pips.
'''
def roll_dice(x):
    count=[0]*6
    for i in x:
        count[i-1]+=1
    roll=math.inf
    for i in x:
        nroll=sum(count)-count[i-1]+count[6-i]#多考虑数字之间的联系，有的时候不一定用数据结构
        if roll>nroll:
            roll=nroll
    return roll


'''
6.Min Cost to Connect All Nodes --Minimum Spanning Tree
Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. The i-th edge connects nodes edges[i][0] and edges[i][1] together. Your task is to augment this set of edges with additional edges to connect all the nodes. Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each other.

Input:

n, an int representing the total number of nodes.
edges, a list of integer pair representing the nodes already connected by an edge.
newEdges, a list where each element is a triplet representing the pair of nodes between which an edge can be added and the cost of addition, respectively (e.g. [1, 2, 5] means to add an edge between node 1 and 2, the cost would be 5).
Example 1:

Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 7
Explanation:
There are 3 connected components [1, 4, 5], [2, 3] and [6].
We can connect these components into a single component by connecting node 1 to node 2 and node 1 to node 6 at a minimum cost of 5 + 2 = 7.
'''
def connect_nodes(e,ne,n):
    #Tuple() is unchangable set is {}
    uf= {}#dic
    #create union find for the initial edges given
    def find(edge):
        uf.setdefault(edge,edge) #if the edge not exit, insert "edge" with the value "edge"
        if uf[edge]!=edge:
            uf[edge]=find(uf[edge])#find the loop
        return uf[edge]
    
    def union(edge1,edge2):
        uf[find(edge1)]=find(edge2)
        
    for e1,e2 in e:
        if find(e1)!=find(e2):
            union(e1,e2)
            
    #sort the new edges by cost
    #if an edge is not part of the minimum spanning tree, then include it, else continue
    Tcost=0
    for v1,v2,cost in sorted(ne, key=lambda x:x[2]):#排序，greedy algorithm
        if find(v1)!=find(v2):
            union(v1,v2)
            Tcost+=cost
            
    if len({find(c) for c in uf})==1 and len(uf)==n:
        return Tcost
    else:
        return -1


#%%
if __name__=='__main__':
    i=input('question number:')
    if i=='2':
        m=[['O','O','O','O'],
            ['D','O','D','O'],
            ['O','O','O','O'],
            ['X','D','D','O']]
        n=[['O','O','O','O'],
            ['O','D','O','O'],
            ['O','D','O','O'],
            ['O','D','D','X'],
            ['O','O','O','O']]
        s=(0,0)
        print(find_island(n,s))
    if i=='3':
        mt=[['S','O','O','S','S'],
            ['D','O','D','O','D'],
            ['O','O','O','O','X'],
            ['X','D','D','O','O'],
            ['X','D','D','D','O']]
        print(find_island2(mt))
    if i=='4':
        start=[0,0]
        po=[[-16,5],[-1,2],[4,3],[10,-2],[0,3],[-5,-9]]
        k=3
        print(knearst_po(start,po,k))
    if i =='5':
        a=[1, 6, 2, 3]
        b=[1,1,2,3,4,5,6,1,2,3]
        print(roll_dice(b))
    if i =='6':
        n = 6
        edges = [[1, 4], [4, 5], [2, 3]]
        new_edges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
        print(connect_nodes(edges,new_edges,n))