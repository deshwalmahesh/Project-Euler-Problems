def div(x):
    lis=[1]
    for j in range(2,x//2+1):
        if x%j==0:
            lis.append(j)
    return(sum(lis))

ami=[]
notami=[]
for i in range(219,10001):
    if i not in notami:
        if i not in ami:
            add=div(i)
            revadd=div(add)
            if i==revadd and add!=i and add!=1:
                ami.append(i)
                ami.append(add)
            else:
                notami.append(add)
                notami.append(revadd)

print(ami)
