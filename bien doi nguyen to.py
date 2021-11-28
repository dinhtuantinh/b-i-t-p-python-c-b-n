import math


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    A = []
    B = []
    for x in a:
        val_left = val_right = x
        while prime(val_left) == False:
            val_left -= 1
        A.append(x-val_left)
        while prime(val_right) == False:
            val_right += 1
        B.append(val_right-x)
    MAX = 0
    for i in range(n):
        MAX = max(MAX, min(A[i], B[i]))
    print(MAX)


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
main()
