import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
n = int(input())
a = [int(i) for i in input().split()]
d=dict()
for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
            d[i]=1
for key in list(d.keys()):
        if(CheckNT(key)):
            print(key," ",d[key])
            
