for test in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    d=dict()
    for i in a:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    for key in list(d.keys()):
        if(d[key]%2 != 0):
            print(key)
            break
