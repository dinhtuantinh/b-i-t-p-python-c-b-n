t = int(input())
F = []
F.append(1)
F.append(1)
for i in range (2,93):
    F.append(F[i-1] + F[i-2])
while t>0:
    a = list(map(int,input().split()))
    for i in range(a[0], a[1] + 1):
        print(F[i-1], end=" ")
    print("\n")
    t=t-1
