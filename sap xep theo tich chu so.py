def tich(n) :      
    tich = 1; 
    while (n > 0) :
        tich *= n % 10; 
        n = n // 10; 
    return tich; 
def sapxep(arr, n) :
    vp = []; 
    for i in range(n) :
        vp.append([tich(arr[i]), arr[i]]);
    vp.sort()
    for i in range(len(vp)) :
        print(vp[i][1], end = " ");
    print()
t=int(input())
for test in range(t):
    n=int(input())
    arr = [int(x) for x in input().split()]
    sapxep(arr, n);
