# A* algorithm

import heapq

g = {
    'A': [('B',1),('C',3)],
    'B': [('D',3),('E',1)],
    'C': [('F',5)],
    'D': [],
    'E': [('F',1)],
    'F': []
}

h = {'A':6,'B':4,'C':4,'D':3,'E':1,'F':0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    seen = set()

    while pq:
        f, cost, node, path = heapq.heappop(pq)
        if node == goal:
            print("Path:", path)
            print("Cost:", cost)
            return
        if node in seen:
            continue
        seen.add(node)

        for n, w in g[node]:
            if n not in seen:
                heapq.heappush(pq, (cost+w+h[n], cost+w, n, path+[n]))

astar('A','F')
