s=str(input())
a=[]
dem=0
res=0
for i in range(len(s)):
    res=res*10+(int)(s[i])
    dem+=1
    if dem==2:
        a.append(res)
        dem=0
        res=0
a=dict.fromkeys(a)
for i in a:
    print(i,end=' ')