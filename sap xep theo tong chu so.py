def sum(n) :      
    sum = 0; 
    while (n > 0) :
        sum += n % 10; 
        n = n // 10; 
    return sum; 
def sapxep(arr, n) :
    vp = []; 
    for i in range(n) :
        vp.append([sum(arr[i]), arr[i]]);
    vp.sort()
    for i in range(len(vp)) :
        print(vp[i][1], end = " ");
    print()
t=int(input())
for test in range(t):
    n=int(input())
    arr = [int(x) for x in input().split()]
    sapxep(arr, n);
