s=str(input())
k=int(input())
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
b=dict.fromkeys(a)
b=sorted(b)
ktr=0
for i in b:
    kq=0
    for j in a:
        if i==j:
            kq+=1
    if kq>=k:
        print(i,kq)
        ktr=1
if ktr==0: print("NOT FOUND")