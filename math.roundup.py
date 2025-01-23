# https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number

# nearest equal or higher multiple of ten

def roundup_v1(x: int, denominator: int = 10):
    return (x // denominator + (x % denominator > 0)) * denominator


def roundup_v2(x: int, denominator: int = 10):
    return math.ceil(x / denominator) * denominator


def roundup_v3(x: int, denominator: int = 10):
    return -(-x // denominator) * denominator
