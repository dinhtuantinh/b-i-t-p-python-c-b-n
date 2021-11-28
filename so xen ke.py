t=int(input())
for test in range(t):
    s=str(input())
    check1=1
    check2=1
    check3=1
    dem=0
    for i in range(len(s)):
        dem+=1
    if dem%2==0:
        check1=0
    if s[0] == s[1]: check2=0
    x=s[0]
    for i in range(len(s)):
        if i%2 == 0 and s[i] != x:
            check3=0
    if check1==1 and check2==1 and check3==1:
        print("YES")
    else:
        print("NO")
