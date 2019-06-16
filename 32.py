li=[]
lj=[]
lk=[]
add=0
for j in range(123,4987):
    for i in range(2,987):
        coun=0
        k=i*j
        sk=str(k)
        si=str(i)
        sj=str(j)
        sw=si+sj+sk
        if len(sw)!=9 or '0' in (sw):
            continue
        else:
            for digi in sw:
                if sw.count(digi)>1:
                    continue
                else:
                    coun+=1
                            
        if (coun==9) and (k not in lk):
            print(i,j,k,sw)
            add=add+k
            lk.append(k)
            li.append(i)
            lj.append(j)
            
print(add,lk)
