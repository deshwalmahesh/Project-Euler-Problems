from isPrime import isPrime
lis=[2]
for i in range(3,775147,2):
    if isPrime(i):
        lis.append(i)
print('finished')
lis=lis[::-1]
for  num in lis:
    if 600851475143%num==0:
        print(num)
        break


