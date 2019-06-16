
def nxt(n):
    if n%2==0:
        return int(n/2)
    else:
        return 3*n+1

max_count=0
max_num=0

lis=[]
ln=[]
for i in range(2,1000000):
    x=i
    count=1
    nxt_num=0
    if i not in lis:
        while nxt_num!=1:
            nxt_num=nxt(x)
            if nxt_num not in lis:
                nxt_num=nxt(x)
                count+=1

            else:    
                count=count+ln[lis.index(nxt_num)]
                lis.append(i)
                ln.append(count)
                break

            x=nxt_num

        
        lis.append(i)
        ln.append(count)

        if count>max_count:
            max_count=count
            max_num=i

print(max_count,
        max_num)
                   
    
    
    

