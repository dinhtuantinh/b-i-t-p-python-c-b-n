import math
n=int(input())
for i in range(0,n+1):
    if (int)(math.pow(2,i))>n:
        print(i-1,(int)(math.pow(2,i-1)))
        break