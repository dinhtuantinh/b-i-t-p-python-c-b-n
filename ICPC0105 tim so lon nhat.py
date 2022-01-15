t=int(input())
for test in range(t):
    s=str(input())
    s=s+" "
    a=[]
    res=0
    n=0
    for i in range(len(s)-1):
        if '0'<=s[i]<='9':
            res=res*10+int(s[i])
            if '0'>s[i+1] or s[i+1]>'9':
                a.append(res)
                n+=1
                res=0
    a.sort()
    print(a[n-1])