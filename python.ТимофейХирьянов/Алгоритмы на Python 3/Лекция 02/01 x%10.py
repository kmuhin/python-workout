flag=False

N = int(input())

for i in range(N):
    x = int(input())
# если число делится без остатка на 10, то истина
# возможно уже был установлен flag в истину, п
    flag = (x%10==0) or flag
    print(flag)
    