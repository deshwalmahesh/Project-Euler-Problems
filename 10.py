from isPrime import isPrime
add=5
for i in range(5,2000000,2):
    if isPrime(i):
        add=add+i

print(add)
