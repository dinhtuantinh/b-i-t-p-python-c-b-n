import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
def dao(n):
    s=str(n)
    if s==s[::-1]: return False
    return True
t=int(input())
for k in range(t):
    n=int(input())
    a=[]
    dem=0
    for i in range(n):
        s=str(i)
        s=s[::-1]
        if CheckNT(i) and CheckNT(int(s)) and dao(i) and int(s)<n: 
            a.append(i)
            dem+=1
    for i in range(dem-1):
        res=str(a[i])
        res=res[::-1]
        for j in range(i+1,dem):
            if str(a[j])==res:
                print(a[i],end=" ")
                print(a[j],end=" ")
    print()
    