
#Common Algorithms
import numpy as np
from collections import deque
from copy import copy,deepcopy

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
        imap=deepcopy(m)
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