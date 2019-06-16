from fractions import gcd
from fractions import Fraction
lis=[]
for n in range(1,1000000):
    for d in range(1,1000000):
        if n>=d or gcd(n,d)!=1:
            continue
        else:
            x=Fraction(n,d)
            lis.append(x)


print(lis[-1])
