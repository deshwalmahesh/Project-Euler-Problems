x=2
count=0
lis=[]
result=0
while x!=200000:
    add=0
    y=str(x)
    for i in y:
        add=add+int(i)**5
    if add==x:
        result+=x
    x+=1


print(result)
