import timeit
import datetime





N = int(input('введи размер массива:'))
print(N)

A=[0]*N
B=[]
for i in range(N):
   A[i]=int(input(f'введи значение {i}:'))

m=0
for i in range(N):
   for k in range(i+1,N):
       if (A[i]*A[k]%26 == 0):
           B.append(f'{A[i]}-{A[k]}')
           m+=1
print(m)

print(B)
start = timeit.default_timer()
end = timeit.default_timer()
print(datetime.timedelta(seconds=end-start))
