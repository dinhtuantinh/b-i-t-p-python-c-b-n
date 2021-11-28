import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
t=int(input())
for test in range(t):
    s=str(input())
    check1=0
    check2=0
    left=""
    right=""
    for i in range(0,3):
        left+=s[i]
    for i in range(len(s)-3,len(s)):
        right+=s[i]
    if CheckNT(int(left)):
        check1=1
    if CheckNT(int(right)):
        check2=1
    if check1==1 and check2==1:
        print("YES")
    else:
        print("NO")
