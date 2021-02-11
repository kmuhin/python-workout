A = [1, 2, 5, 3, 2, 8, 11, 6, 0]
print(A)

B = []

# получить новый список из А четных чисел в квадрате
# через for
for x in A:
    if x % 2 == 0:
        B.append(x ** 2)
print(B)

# через comprehensions
C = [x ** 2 for x in A if x % 2 == 0]
print(C)

# тернарный оператор if
D = [0 if x<8 else x**2 for x in A if x % 2 == 0]
print(D)