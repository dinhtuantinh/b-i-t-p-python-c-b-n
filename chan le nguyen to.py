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
    check3=0
    sum=0
    for i in range(len(s)):
        if i%2==0 and int(s[i])%2!=0:
            check1=0
            break
    for i in range(len(s)):
        if i%2!=0 and int(s[i])%2==0:
            check2=0
            break
    for i in range(len(s)):
        sum+=int(s[i])
    if CheckNT(sum): check3=1
    if check1==1 and check2==1 and check3==1:
        print("YES")
    else:
        print("NO")
    
