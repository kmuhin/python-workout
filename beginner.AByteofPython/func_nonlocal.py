def func_outer() -> object:
    x: int = 2
    print('x equals', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('local x has changed to', x)


a: object = func_outer()
print(a)
