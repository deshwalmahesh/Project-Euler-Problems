from palin import palin
lis=[]
for i in range(0,1000000):
    if palin(str(i)):
        bini=str(bin(i))
        bini=bini[2::]
        if palin(bini):
            lis.append(i)

print(lis,sum(lis))
