#BFS

from collections import deque
g={'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}
q=deque(['A']); v={'A'}
while q:
    n=q.popleft()
    print(n,end=" ")
    for x in g[n]:
        if x not in v:
            v.add(x); q.append(x)

