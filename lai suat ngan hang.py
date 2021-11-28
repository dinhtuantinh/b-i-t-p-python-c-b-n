t = int(input())
for test in range(t):
    n,x,m=[float(x) for x in input().split()]
    dem=0
    while n<m:
        n=n+n*x/100
        dem+=1
    print(dem)
        
    
