day=1
date=1
month=1
year=1900
m31=[1,3,5,7,8,10,12]
m30=[4,6,9,11]
count=0
while year<2001:
    if day%7==0:
        if date==1 and year>1900:
            count+=1
        day=0
    if date>=28 and month==2:
        if date==28 and year%4!=0:
            month+=1
            date=1
            day+=1
            continue
        elif date==29 and year%4==0 and year>1900:
            date=1
            day+=1
            month+=1
            continue
        
        elif date==28 and year==1900:
            month+=1
            day+=1
            date=1
            continue
            
        
    elif (date==30 and month in m30):
            month+=1
            date=1
            day+=1
            continue

    elif (date==31 and month in m31):
        if month<12:
            month+=1
            date=1
            day+=1
        else:
            month=1
            year+=1
            date=1
            day+=1
        continue
    day+=1
    date+=1
        
print(count)   
