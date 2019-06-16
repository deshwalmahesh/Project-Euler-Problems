dic={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
     16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',1000:'one thousand'}

add=0

def find(x):
    #print(dic[x])
    return(len(dic[x]))

num=''
for i in range(1,1001):
    
    if i>20 and i<100 and i%10!=0:
        rem=i%10
        quo=1//10
        num=num+dic[i-rem]+' '+dic[rem]
        #add+=find(quo)+find(rem)

    elif i>99 and i<1000:
        num=num+dic[i//100]+' hundred'
        quo=i//100
        rem=i%100
        if i%100==0:
            continue
        else:           
            if rem>20 and rem%10!=0:
                num=num+' and '+dic[rem-rem%10]+ dic[rem%10]
                #add+=find(rem)
            else:
                num=num+' and '+dic[rem]

    else:
        num=num+dic[i]
        #print(num)
        #add+=find(i)

    

#print(num)
    
