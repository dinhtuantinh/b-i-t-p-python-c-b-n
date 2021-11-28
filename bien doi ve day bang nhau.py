n = int(input())
a = [int(x) for x in input().split()]
MIN = sum(a)
val = a[0]
for x in a:
    res = 0
    for y in a:
        res += abs(x-y)
    if MIN > res:
        MIN = res
        ans = x
print(MIN, ans, sep=" ")
