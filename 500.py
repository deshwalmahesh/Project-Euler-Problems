def fact_num(x):
    count=1
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
                count+=1
        else:
            continue
    return(count*2)
limit=2**500500
i=121
while True:
    if fact_num(i)==limit:
        print("success",i%500500507)
        
        break
    
    i+=1
