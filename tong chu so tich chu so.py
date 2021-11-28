t=int(input())
for test in range(t):
    s=str(input())
    sum=0
    tich=1
    check=0
    for i in range(len(s)):
        if i%2==0:
            sum+=int(s[i])
    for i in range(len(s)):
        if i%2!=0 and int(s[i])!=0:
            check=1
            break
    if check==0:
        print(sum,end=" ")
        print("0")
    else:
        print(sum,end=" ")
        for i in range(len(s)):
            if i%2!=0:
                if int(s[i])==0:
                    continue
                else:
                    tich=tich*int(s[i])
        print(tich)
                
