import sys
import time
from functools import wraps


def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        ts = time.perf_counter()
        result = f(*args, **kwargs)
        te = time.perf_counter()
        print(f'{f.__module__}.{f.__name__}  took: {te - ts:10f}', file=sys.stderr)
        return result

    return wrap
