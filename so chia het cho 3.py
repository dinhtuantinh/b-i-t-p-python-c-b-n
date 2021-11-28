t=int(input())
for test in range(t):
    s=str(input())
    sum=0
    for i in range(len(s)):
        sum+=int(s[i])
    if sum%3==0:
        print("YES")
    else:
        print("NO")
