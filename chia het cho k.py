a,k,n=(int(x) for x in input().split())
c=k-(a%k)
ktr=0
for i in range(c,n-a+1,k):
    if(a+i)%k==0:
        print(i,end=" ")
        ktr=1
if ktr==0:
    print(-1)
