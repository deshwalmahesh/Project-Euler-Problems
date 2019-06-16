from math import sqrt

for a in range(334,997):
    for b in range(449,2,-1):
        c=(sqrt(a*a+b*b))
        if a+b+c==1000:
            print(a*b*c)
