T=int(input())
for t in range(T):
    s=input()
    check=1
    for i in s:
        if i!='4' and i!='7':
            check=0
            break;
    if check:
        print("YES")
    else:
        print("NO")
