import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
a = list(map(int,input().split()))
n = a[0]
x = a[1]
arr1 = []
arr2 = []
cnt, i =0, 2
while cnt <= n:
    if CheckNT(i):
        arr1.append(i)
        cnt += 1
    i += 1
arr2.append(x)
res = ""
for j in range(n + 1):
    res += (str(arr2[j]) + " ")
    arr2.append(arr2[j] + arr1[j])
print(res)
