from fractions import Fraction
product=1
for denom in range(12,100):
    for num in range(11,denom):
        d=str(denom)
        n=str(num)
        if denom%10==0 or num%10==0 or num%11==0 or denom%11==0:
            continue
        else:
            
            if n[0] in d:
                d=(d.replace(n[0],''))
                n=(n.replace(n[0],''))
                if Fraction(num,denom)==Fraction(int(n),int(d)):
                    print("######### ",num,denom,n,d," ##########")
                    break


            elif n[1] in d:
                d=d.replace(n[1],'')
                n=n.replace(n[1],'')

                if Fraction(num,denom)==Fraction(int(n),int(d)):
                    product*=Fraction(num,denom)
                    break


print(product.denominator)
