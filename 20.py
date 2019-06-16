def fact(n):
    fac=1
    for i in range(n,0,-1):
        fac=fac*i
        n-=1
    return(fac)

fac=str(fact(100))
add=0
for i in fac:
    add+=int(i)

print(add)
    
    
