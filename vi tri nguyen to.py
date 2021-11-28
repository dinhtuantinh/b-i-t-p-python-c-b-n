import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
t=int(input())
for test in range(t):
    s=str(input())
    check1=1
    check2=1
    for i in range(len(s)):
        if CheckNT(i) and CheckNT(int(s[i]))==False:
            check1=0
            break
    for i in range(len(s)):
        if CheckNT(i)==False and CheckNT(int(s[i])):
            check2=0
            break
    if check1==1 and check2==1:
        print("YES")
    else:
        print("NO")
