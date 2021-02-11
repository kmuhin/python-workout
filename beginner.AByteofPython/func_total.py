def total(initial=5, *numbers, **keywords):
    count: int = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count


print(total(1,2,3,vegetables=1,fruits=1))
