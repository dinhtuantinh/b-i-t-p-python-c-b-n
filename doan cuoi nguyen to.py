import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
t=int(input())
for test in range(t):
    s=str(input())
    check=0
    res=""
    for i in range(len(s)-4,len(s)):
        res+=s[i]
    if CheckNT(int(res)):
        check=1
    if check==1:
        print("YES")
    else:
        print("NO")
