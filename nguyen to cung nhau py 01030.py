import math
def USCLN(a, b):
    if b == 0:
        return a
    return USCLN(b, a % b)
a = [int(i) for i in input().split()]
n=a[0]
k=a[1]
dem=0
for i in range(pow(10,k-1),pow(10,k),1):
    if USCLN(i, n)==1:
        dem+=1
        if dem>10:
            print()
            dem=1
        print(i,end=" ")
