import math

data=[['Sunny','No'],['Sunny','No'],
      ['Overcast','Yes'],['Rain','Yes'],
      ['Rain','No']]

def e(d):
    y=sum(1 for r in d if r[1]=='Yes')
    n=len(d)-y
    return -sum((c/len(d))*math.log2(c/len(d)) for c in [y,n] if c)

def g(d):
    vals=set(r[0] for r in d)
    return e(d)-sum((len([r for r in d if r[0]==v])/len(d))*
           e([r for r in d if r[0]==v]) for v in vals)

print("Entropy:",round(e(data),3))
print("Gain:",round(g(data),3))

print("\nOutlook")
for x in set(r[0] for r in data):
    print(x,"->",max([r[1] for r in data if r[0]==x],
          key=[r[1] for r in data if r[0]==x].count))
