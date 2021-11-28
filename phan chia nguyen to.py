import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
n=int(input())
a=[int(i) for i in input().split()]
d=dict.fromkeys(a)
b=list(d)
tong1=0
dem=-1
check=0
for i in b:
    tong1+=i
    dem+=1
    if(CheckNT(tong1))==1:
        tong2=0
        for j in range(dem+1,len(b)):
            tong2+=b[j]
        if CheckNT(tong2)==1:
            print(dem)
            check=1
            break
if check==0:
    print("NOT FOUND")
