n=int(input())
arr=[int(i) for i in input().split()]
dem=0
for i in range(n):
    for j in range(n):
        if (i<j) and (arr[i]>arr[j]):
            dem=dem+1
print(dem)
