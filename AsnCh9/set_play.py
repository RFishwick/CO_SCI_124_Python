
myset1 = set()
print(myset1)

myset1 = set(['a', 'b', 'c'])

print(myset1)

myset2 = set('abcd')

print(myset2)

for val in myset2:
    print(val)

print('\n', myset2.difference(myset1))