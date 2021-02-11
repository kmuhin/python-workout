x = 50

def func():
    global x

    print('x equal', x)
    x = 2
    print('Chage global var x to', x)

func()
print('Value x is', x)
