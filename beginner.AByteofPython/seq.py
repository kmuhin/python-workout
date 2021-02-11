shoplist = ['apples', 'mango', 'carrot', 'bananes']
name = 'swaroop'

print('Item 0 -', shoplist[0])
print('Item 1 -', shoplist[1])
print('Item 2 -', shoplist[2])
print('Item 3 -', shoplist[3])

print('Item -1 -', shoplist[-1])
print('Item -2 -', shoplist[-2])
print('Char 0 -', name[0])

if 's'.upper() in name.upper():
    print('true')

print('Items  1 -3 ', shoplist[1:3])
print('Items 2 - end ', shoplist[2:])
print('Items 1 - -1 ', shoplist[1:-1])
print('Items start - end', shoplist[:])
