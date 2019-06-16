def fact(x):
    x=int(x)
    fac=1
    while x>0:
        fac*=x
        x-=1
    return fac

