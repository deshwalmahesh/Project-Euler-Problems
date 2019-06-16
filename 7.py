lis=[2,3,5,7,11,13]
count=6

from isPrime import isPrime #see isPrime file in this folder. this checks if a no is prime or not


for num in range(15,100000000000000,2):
    if isPrime(num):
        count+=1
        lis.append(num)
    if count==10001:
        break
        

        
                   
print(lis[-1])        
                   
                   
