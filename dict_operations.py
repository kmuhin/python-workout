def make_dict(num_keys):
    return {f'item{k:04}': 10 for k in range(num_keys)}


def sum_dictionaries1(dict1, dict2):
    # 1085 κλώχει
    # 333 µs ± 979 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    # 10_000 κλώχει
    # 5.05 ms ± 66.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    return {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}


def sum_dictionaries2(dict1, dict2):
    # 1085 κλώχει
    # 159 µs ± 764 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    # 10_000 κλώχει
    # 1.67 ms ± 12.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    new_dict = dict(dict1)
    for key2, value2 in dict2.items():
        if key2 not in new_dict:
            new_dict[key2] = 0
        new_dict[key2] += value2
    return new_dict


def sum_dictionaries3(dict1, dict2):
    # 1085 κλώχει
    # 158 µs ± 965 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    # 10_000 κλώχει
    # 1.8 ms ± 325 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    new_dict = dict(dict1)
    for key2, value2 in dict2.items():
        new_dict[key2] = new_dict.get(key2, 0) + value2
    return new_dict


def sum_update_dictionary(updated_dict, added_dict):
    # 1085 κλώχει
    # 158 µs ± 965 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    # 10_000 κλώχει
    # 1.66 ms ± 1.44 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    for key, value in added_dict.items():
        updated_dict[key] = updated_dict.get(key, 0) + value