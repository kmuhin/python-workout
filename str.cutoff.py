from functools import wraps
import time

id="tr_item_261634688"

enable_wrap_timing=True

def wrap_timing(f):
    if not enable_wrap_timing:
        return f
    @wraps(f)
    def wrap(*args, **kwargs):
        ts = time.perf_counter()
        result = f(*args, **kwargs)
        te = time.perf_counter()
        print(f'func:{f.__name__[:20]:20}  took: {te - ts:10f}')
        return result
    return wrap


@wrap_timing
def str_remove(remove, string):
    return string.replace(remove, '')

@wrap_timing
def str_last_delim(string, delim=''):
    _, result = string.rsplit(delim, 1)
    return result
@wrap_timing
def str_slice2endfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(string, index=''):
    return string[index:]

if __name__ == '__main__':
  print(str_remove('tr_item_', id))
  print(str_last_delim(id, '_'))
  print(str_slice2endfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(id, 8))