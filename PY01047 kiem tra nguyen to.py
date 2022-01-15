import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
t=int(input())
for k in range(t):
    s=str(input())
    n=""
    for i in range(len(s)-1,len(s)-5,-1):
        n+=s[i]
    n=n[::-1]
    res=int(n)
    if(CheckNT(res)): print("YES")
    else: print("NO")