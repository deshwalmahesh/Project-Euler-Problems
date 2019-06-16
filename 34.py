from fact import fact

i=3
res=0
while True:
    add=0
    for digit in str(i):
        add+=fact(digit)
    if add==i:
        print(i)
        res+=i
        print(res)
    i+=1
