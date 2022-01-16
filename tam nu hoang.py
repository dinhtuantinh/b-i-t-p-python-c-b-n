a=[]
b=[]
for i in range(8):
    p,q=(int(i) for i in input().split())
    a.append(p)
    b.append(q)
check=True
x,y=dict(),dict()
while check:
    for i in a:
        if not(i in x):
            x[i]=0
        x[i]+=1
        if x[i]>1:
            check=False
            break
    if check==False:
        break
    for i in b:
        if not(i in y):
            y[i]=0
        y[i]+=1
        if y[i]>1:
            check=False
            break
    if check==False:
        break
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            m=abs(a[i]-a[j])
            n=abs(b[i]-b[j])
            if m==n:
                check=False
                break
        if(check==False):
            break
    break
if check==True:
    print("NO")
else:
    print("YES")