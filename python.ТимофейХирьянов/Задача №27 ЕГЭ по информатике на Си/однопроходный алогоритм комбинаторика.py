N=int(input(f'введи значение массива:'))

m=0
k1,k2,k13,k26=0,0,0,0

for i in range(N):
    x=int(input(f'введи значение {i}:'))
    if (x%26 == 0):
        print('%26')
        k26+=1
    elif (x%13  == 0):
        print('%13')
        k13+=1
    elif (x%2  == 0):
        print('%2')
        k2+=1
    else:
        k1+=1  

m = k26*(k26-1)/2 + k26*(k1+k2+k13) + k2*k13
print(f'k1={k1}\nk2={k2}\nk13={k13}\nk26={k26}\n')
print(m)
