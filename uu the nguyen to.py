import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
t=int(input())
for test in range(t):
    s=str(input())
    dem=0
    check=1
    for i in range(len(s)):
        if CheckNT(int(s[i])):
            dem+=1
    if dem<=len(s)/2:
        check=0
    if CheckNT(len(s)) and check==1:
        print("YES")
    else:
        print("NO")
