i=0
while i<10: # Заголовок цикла
    print(i,end=' ')  # тело цикла
    i+=1              # тело цикла
    if i == 5:
         print("\n5")
         break
# итерация - процесс выполнения тела цикла
# else выполняется, если не выполняется break или исключение
else:
    print('end of while')

i =  0
while i < 10:
  y =  0
  while y < 10:
     print(f'{i}-{y}',end=' ')
     y+=1
  print()
  i+=1