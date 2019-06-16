from math import gcd
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]   #will work for an int array of any length
lcm = a[0]
for i in a[1:]:
  lcm = lcm*int(i/gcd(lcm, i))
print (lcm)
