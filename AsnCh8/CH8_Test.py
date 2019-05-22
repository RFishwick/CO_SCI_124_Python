name = 'Juliet'
for ch in name:
    print(ch)

print('name:', name, '\n')

for i in range(5, -1, -1):
    print(i)
    print(name[i], '\n')

S = "boring"
if S.endswith('ing'):
    print("Ends with 'ing'")

S = "boring"
if S.find('ori'):
    print("contains 'ori'")

print('lstrip:', name.lstrip('J'))
print('name:', name, '\n')

city = 'New York'
print('slice: ', city[5:5])

S = "This is a long sentence.  This is a short one.  This is another one."
print(S)

print(S.split('.'))
