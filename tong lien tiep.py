import math
def dem(n):
    n=n*2
    x=0;y=0;d=0;
    m=int(math.sqrt(n))
    for i in range(2,m+1,1):
        if n % i==0:
            y=n//i
            if (y-i)%2!=0:
                d+=1
    return d
t=int(input())
for test in range(t):
    n=int(input())
    print(dem(n))
    
