import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
n = int(input())
a = [int(i) for i in input().split()]
dem=0
for i in range(n):
    if CheckNT(a[i])==False:
        dem+=1
print(dem)
