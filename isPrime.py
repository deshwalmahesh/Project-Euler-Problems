def isPrime(x):
    x=int(x)

    if x==2:
        return True
    
    if x<2 or x%2==0:
        return False
    

    else:

        for i in range(3,int(x**0.5)+1):  #use this function only with step 2 and start 3 and more
            if x%i==0:
                return False
        else:
            return True
