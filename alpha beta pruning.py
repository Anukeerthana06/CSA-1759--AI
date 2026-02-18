# Alpha-Beta Pruning

import math
s = [3,5,6,9,1,2,0,-1]

def ab(d,n,a,b,maxi,h):
    if d==h: return s[n]
    if maxi:
        v=-9
        for i in range(2):
            v=max(v,ab(d+1,n*2+i,a,b,False,h))
            a=max(a,v)
            if b<=a: break
        return v
    else:
        v=9
        for i in range(2):
            v=min(v,ab(d+1,n*2+i,a,b,True,h))
            b=min(b,v)
            if b<=a: break
        return v

h=int(math.log2(len(s)))
print("Optimal value:",ab(0,0,-9,9,True,h))
