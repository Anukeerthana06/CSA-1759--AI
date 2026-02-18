N = 8

def solve(b, c):
    if c == N: return True
    for r in range(N):
        if all(b[r][i]==0 for i in range(c)) and \
           all(b[r-i][c-i]==0 for i in range(1,min(r,c)+1)) and \
           all(b[r+i][c-i]==0 for i in range(1,min(N-r-1,c)+1)):
            b[r][c] = 1
            if solve(b, c+1): return True
            b[r][c] = 0
    return False

b = [[0]*N for _ in range(N)]
solve(b, 0)
for i in b: print(i)
