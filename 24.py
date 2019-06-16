import itertools

y=list(itertools.permutations('0123456789'))
print(int(''.join(y[999999])))
