#Depth-First Search

g={'a':set(['b','c']),'b':set(['a','d','e']),'c':set(['a','f']),'d':set(['b']),'e':set(['b','f']),'f':set(['c','e'])}

def dfs(graph,start):
    visited, stack= set(), [start]

    while stack:
        vertex= stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
            print('Visited:',visited,'Stacked:',stack)
    return visited

print(dfs(g,'a'))
