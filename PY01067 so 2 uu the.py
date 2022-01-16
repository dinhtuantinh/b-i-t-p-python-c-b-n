def check(n):
    s=str(n)
    a=[]
    check1=1;check2=0
    for i in range(len(s)):
        if int(s[i])>2 and int(s[i])<=9:
            check1=0
            break
    for i in range(len(s)):
        a.append(int(s[i]))
    if a.count(2)>len(s)//2:
        check2=1
    if check1==1 and check2==1: return True
    else: return False
t=int(input())
for k in range(t):
    n=int(input())
    dem=0
    i=2
    while dem<n:
        if check(i): 
            print(i,end=" ")
            dem+=1
        i+=1
    print()