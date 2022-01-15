def tinhgiaithua(n):
    giai_thua = 1
    if (n == 0 or n == 1):
        return giai_thua
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua
t=int(input())
for k in range(t):
    n=int(input())
    s=str(n)
    sum=0
    for i in range(len(s)):
        sum+=tinhgiaithua(int(s[i]))
    if sum==n:print("Yes")
    else: print("No")