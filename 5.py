flag=False
for i in range(999,100,-1):
    for j in range(999,i-100,-1):
        x=str(i*j)
        if x==x[::-1]:
            print(i,j)
            flag=True
            break
    if flag:
        break
