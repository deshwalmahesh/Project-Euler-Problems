a=1
d=1
n=1

def no_div(no):
    count=1
    for i in range(2,int(no**0.5)+1):
        if no%i==0:
            count+=1
    return(count*2)

while True:
    no=int((n/2)*(2+(n-1)))
    n+=1
    if no_div(no)>500:
        print(no)
        break
    
