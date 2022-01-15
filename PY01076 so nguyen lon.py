def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)
def bscnn(a, b):
    return int((a * b) / uscln(a, b))
t=int(input())
for i in range(t):
    a = int(input())
    b = int(input())
    print(uscln(a,b))