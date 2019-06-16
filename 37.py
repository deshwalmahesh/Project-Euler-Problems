def isPrime(x):
    x=int(x)

    if x==2:
        return True
    
    elif x<2 or x%2==0:
        return False
    

    else:
        for i in range(3,int(x**0.5)+1):  #use this function only with step 2 and start 3 and more
            if x%i==0:
                return False
        else:
            return True

count=0
i=10
lis=[]
while count!=11:
    num=0
    stri=str(i)
    if '0' in stri or '4' in stri or '6' in stri or '8' in stri:
        i+=1
        continue
    else:
        if isPrime(i):
            for limit in range(len(stri)-1):
                left=stri[limit+1::]
                right=stri[0:len(stri)-limit-1]
                if not(isPrime(left) and isPrime(right)):
                    i+=1
                    continue
                else:
                    num+=1
                    
    if num==len(stri)-1:
        count+=1
        print(i)
        lis.append(i)
    i+=1
print(sum(lis))        
