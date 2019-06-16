from itertools import permutations
from isPrime import isPrime
import time

cp=[2,3,5]
for i in range(7,1000000,2):
    count=0
    stri=str(i)
    if '2' in stri or '4' in stri or '5' in stri or '6' in stri or '8' in stri or '0'in str(i):
        continue
    else:
        if isPrime(stri):
            for j in range(len(stri)):
                no=stri
                if isPrime(no):
                    count+=1
                    stri=stri[1::]+stri[0]
                else:
                    break
            if count==len(stri):
                cp.append(i)
print(cp)
