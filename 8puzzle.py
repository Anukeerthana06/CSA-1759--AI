from collections import deque
s = ((1,2,3),(4,0,6),(7,5,8))
g = ((1,2,3),(4,5,6),(7,8,0))
def print_matrix(state):
    for row in state:
        print(*row)
    print()
q = deque([s])
v = {s}
count = 0
while q:
    s = q.popleft()
    if count < 2:
        print("Current State:")
        print_matrix(s)
        count += 1
    if s == g:
        print("Goal State:")
        print_matrix(s)
        break
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                x, y = i, j
    for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0 <= nx < 3 and 0 <= ny < 3:
            t = [list(r) for r in s]
            t[x][y], t[nx][ny] = t[nx][ny], t[x][y]
            t = tuple(map(tuple, t))
            if t not in v:
                v.add(t)
                q.append(t)
