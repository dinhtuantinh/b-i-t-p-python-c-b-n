t =int(input())
for i in range(t):
    s=str(input())
    check1=0
    check2=0
    tong=0
    for j in range(len(s)):
        tong+=int(s[j])
    if tong%10!=0: check1=1
    for j in range(len(s)-1):
        tmp=abs(int(s[i])-int(s[i+1]))
        if tmp!=2:
            check2=1
            break
    if check1==0 and check2==0:
        print("YES")
    else: print("NO")
    #print(tong)
