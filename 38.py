def pandi(x):
    x=str(x)
    if len(x)==9 and '0' not in x:
        for i in x:
            if x.count(i)>1:
                return False
            else:
                return True

    else:
        return False


for i in range(1,1000):
