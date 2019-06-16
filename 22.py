with open ('names.txt','r') as file:
    lis=file.readline().split(',')

lis.sort()
total=0
for i in range(0,len(lis)):
    add=0
    x=lis[i].strip('"')
    for word in x:
        add+=ord(word)-64
    total+=add*(i+1)


print(total)





