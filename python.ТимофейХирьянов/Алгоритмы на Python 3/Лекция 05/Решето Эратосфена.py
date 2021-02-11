''' 
Индексы массива -  искомые простые числа
Заполняю  массив значениями True - простые числа
Числа 0,1 - исключения.
Далее прохожу по массиву от k=2 до N с шагом 1.
Помечаю индексы кратные k как False - составные числа.
Прохожу по массиву от m=2*k до N с шагом k
Пример:
k1=3
m1=2*3=6, m2=2*3+3=9, m3=2*3+3+3=12 ...
[True, True, True, True, True, True, True, True, True, True]
[0     1     2     3     4     5     6     7     8     9  ]
0, 1 - непростые = False
2 - 2*2=4 +2=6 +2=8
 0      1                  4            6
[False, False, True, True, False, True, False, True, True, True]
3 - 3*2=6 +3=9
                                        6                  9
[False, False, True, True, False, True, False, True, True, False]
4 - 4*2=8
                                                     8
[False, False, True, True, False, True, False, True, False, False]
'''

# для наглядности
def print_composite(list_of_bln, list_of_composite=[]):
    # печатаю False, если индекс есть в списке list_of_composite 
    # либо 5 прочерков
    for index, key in enumerate(list_of_bln):
        if index not in list_of_composite:
            print('-'*5,end=' ')
        else:
            print(str(key).ljust(5), end=' ')
    print()
    
# кол-во чисел от нуля
N=20

# делаю список размера N все элементы которого True
A=[True]*N
# Числа 0,1 - к простым не относятся, помечаю False
A[0]=A[1]=False
# печатаю шапку с числами
print(' '*5+' '.join([str(i).ljust(5) for i in range(N)]))
# печатаю список до алгоритма
print(' '*5, end='')
print_composite(A,[*range(N)])
# пошла работа
for k in range(2,N):
    composite = []
    if A[k]:
        for m in range(2*k,N,k):
            A[m]=False
            composite.append(m)
        print(str(k).ljust(3),end=': ')
        # печатаю только текущие список простых чисел
        print_composite(A,composite)
# печатаю результат
for k in range(N):
   print(f'{k:2}','-',"простое" if A[k] else "составное")