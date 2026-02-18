#DFS

g={1:[2,3],2:[4],3:[5],4:[],5:[]}

def dfs(n,v=set()):
    print(n,end=" "); v.add(n)
    for x in g[n]:
        if x not in v: dfs(x,v)

dfs(1)
