# Определить наибольшее и наименьшее введеное значение переменной s,
# при котором программа выведет число 64. В ответ запишите сумму этих чисел.
#
# s = int(input())
# n = 1
# while s < 200:
#     s = s + 25
#     n = n*2
# print(n)
# математически система уравнений:
# n = 64 = 2 в степени 6, должно пройти 6 итераций.
# s+25*6 >= 200
# s+25*5 < 200
# s >=50, s< 75
# s = [50,74], sum = 124

n_first = None
n_last = None
for i in range(0, 500):
    # s = int(input())
    s = i
    n = 1
    while s < 200:
        s = s + 25
        n = n * 2
    if n == 64:
        n_last = i
        if n_first is None:
            n_first = i

print('Диапазон значений:', n_first, '-', n_last)
if n_first is None:
    print('Ответ не найдет')
else:
    print('Ответ:', n_first + n_last)
