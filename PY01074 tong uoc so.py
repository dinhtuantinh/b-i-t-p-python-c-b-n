import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
def Snto(n):
    s=0
    for i in range(2,int(math.sqrt(n))+1):
        dem=0
        if n%i==0 and CheckNT(i):
            while n%i==0:
                dem+=1
                n/=i
        s+=i*dem
    if n>1:s+=n
    return s
t=int(input())
sum=0
for k in range(t):
    n=int(input())
    sum+=Snto(n)
print(int(sum))