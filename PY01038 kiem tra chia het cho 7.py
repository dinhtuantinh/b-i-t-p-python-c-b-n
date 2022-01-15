def dao(n):
    m=str(n)
    m=m[::-1]
    return int(m)
t=int(input())
for test in range(t):
    n=int(input())
    count=1
    check=0
    if n%7==0: print(n)
    else:
        while(count<=1000):
            s=n+dao(n)
            if s%7==0:
                print(s)
                check=1
                break
            else:
                count+=1
                n=s
        if check==0: print(-1)