add=0
minus=0
for i in range (1,101):
    add=add+(i**2)
    minus=minus+i

minus=minus**2
print(add-minus)
