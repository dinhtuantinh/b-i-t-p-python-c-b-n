def reVal(num):
    if (num >= 0 and num <= 9):
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))
def strev(str):
    len1 = len(str)
    for i in range(int(len1 / 2)):
        temp = str[i]
        str[i] = str[len1 - i - 1]
        str[len1 - i - 1] = temp
def fromDeci(res, base, inputNum):
    index = 0
    while (inputNum > 0):
        res+= reVal(inputNum % base)
        inputNum = int(inputNum / base)
    res = res[::-1]
    return res
t=int(input())
for k in range(t):
    a=[int(i) for i in input().split()]
    n=a[0]
    m=a[1]
    res = ""
    print(fromDeci(res, m, n))