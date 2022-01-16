n = int(input())
arr ={}
for i in range (n):
    a = list(input().split())
    arr[a[0]] = a[1:]
m = int(input())
for t in range (m):
    b = input()
    for i, j in arr.items():
        if b in j:
            print(i)