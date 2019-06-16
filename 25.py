a=1
b=1
c=0
ln=0
count=2
while True:
    c=a+b
    a=b
    b=c
    count+=1
    if len(str(c))==1000:
        print(count)
        break
