print("Simple assignment")
shoplist = ['Apples', 'Mango', 'Carrot', 'Bananes']
mylist = shoplist
del shoplist[0]
print('shoplist:', shoplist)
print('mylist:', mylist)
print('Copy with slice')
mylist=shoplist[:]
del mylist[0]
print('shoplist:', shoplist)
print('mylist:', mylist)
