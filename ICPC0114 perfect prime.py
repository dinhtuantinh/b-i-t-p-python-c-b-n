import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
t=int(input())
for k in range(t):
    n=int(input())
    check1=0
    check2=0
    check3=0
    check4=1
    s=str(n)
    if CheckNT(n): check1=1
    k=int(s[::-1])
    if CheckNT(k): check2=1
    sum=0
    for i in range(len(s)):
        sum+=int(s[i])
    if CheckNT(sum): check3=1
    for i in range(len(s)):
        if CheckNT(int(s[i]))==False: 
            check4=0
            break
    if check1==1 and check2==1 and check3==1 and check4==1:
        print("Yes")
    else: print("No")