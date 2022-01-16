n=int(input())
a=n%10
n=n//10
b=n%10
n=n//10
if n<b<a:
    print("YES")
else:
    print("NO")