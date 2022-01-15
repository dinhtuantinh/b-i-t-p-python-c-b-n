import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
t=int(input())
for k in range(t):
    s=str(input())
    check1=0;check2=0
    if CheckNT(len(s)): check1=1
    count1=0;count2=0
    for i in range(len(s)):
        if(CheckNT(int(s[i]))): count1+=1
        else: count2+=1
    if count1>count2:check2=1
    if check1==1 and check2==1:
        print("YES")
    else: print("NO")