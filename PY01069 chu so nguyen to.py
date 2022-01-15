import math
def kt(s):
    check1=1
    if int(s[len(s)-1])%2==0:check1=0
    check2=1
    for i in range(len(s)):
        if s[i]=='0' or s[i]=='1' or s[i]=='4' or s[i]=='6' or s[i]=='8' or s[i]=='9':
            check2=0
            break
    check3=0;check4=0;check5=0;check6=0;check7=0
    for i in range(len(s)):
        if s[i]=='2':
            check4=1
            break
    for i in range(len(s)):
        if s[i]=='3':
            check5=1
            break
    for i in range(len(s)):
        if s[i]=='5':
            check6=1
            break
    for i in range(len(s)):
        if s[i]=='7':
            check7=1
            break
    if check4==1 and check5==1 and check6==1 and check7==1: check3==1
    if check1==1 and check2==1 and check3==1:
        return True
    else: return False
n=int(input())
x=int(math.pow(10,n))
for k in range(1000,x):
    if kt(str(k)): print(k)