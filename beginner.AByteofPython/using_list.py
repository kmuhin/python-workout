shoplist = ['apples', 'mango', 'carrot', 'bananes']

print('i have to do ', len(shoplist), 'purchases')

print('purchases:', end='')
for item in shoplist:
    print(item, end=' ')

print('\nAlso i have to buy rice.')
shoplist.append('rice')
print('now my list looks like this: ', shoplist)

print('I sort my list')
shoplist.sort()
print('The sorted list looks like this: ', shoplist)

print('First I need to buy this: ', shoplist[0])

olditem=shoplist[0]
del shoplist[0]
print('I have bought', olditem)
print('Now my list looks like this: ', shoplist)
