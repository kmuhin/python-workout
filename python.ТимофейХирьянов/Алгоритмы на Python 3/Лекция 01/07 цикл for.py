# for - списочный цикл.
for x in 1,5,2,7:
  print(f'{x:2}:',x**2)
else:
  print('end of for')
# range(start,stop,step)
# генератор последовательности
for i in range(10):
  print(f'{i:2}',end=' ')
print()

for i in range(10,1,-1):
  print(f'{i:2}',end=' ')