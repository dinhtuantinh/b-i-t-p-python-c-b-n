count = 0
A = []
while count < 10:
    s = [int(x) for x in input().split()]
    for i in s:
        tmp = i % 42
        if tmp not in A:
            A.append(tmp)
    count += len(s)
print(len(A))
