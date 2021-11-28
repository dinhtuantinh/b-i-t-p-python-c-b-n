#round(a,2)
import decimal
from decimal import Decimal, getcontext
t=int(input())
for test in range(t):
    n=int(input())
    s=0
    if n%2==0:
        for i in range(2,n+1,2):
            s+=1.00/i
    else:
        for i in range(1,n+1,2):
            s+=1.00/i
    print(Decimal(s).quantize(Decimal('1.000000')))
