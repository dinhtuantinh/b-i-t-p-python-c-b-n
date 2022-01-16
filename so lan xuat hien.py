x = {}
for i in input().split():
    x[i] = x.get(i, 0) + 1
    print(x[i] - 1, end=" ")