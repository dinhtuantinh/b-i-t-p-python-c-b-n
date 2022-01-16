n = int(input())
arr ={}
List = []
for i in range(n):
    a = list(input().split())
    for t in range(len(a)):  
        if a[t] not in arr:
            arr[a[t]] = 0
        arr[a[t]] += 1
for k,v in arr.items():
    if v >= max(arr.values()):
        List.append(k)
print(sorted(List)[0])