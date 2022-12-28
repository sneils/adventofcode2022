from json import loads as json_loads
from functools import cmp_to_key


def aslist(x):
    if isinstance(x, list):
        return x
    return [x]


def compare(a, b):
    if type(a) != type(b):
        return compare(aslist(a), aslist(b))

    if isinstance(a, int):
        return a < b

    for i in range(min(len(a), len(b))):
        if len(aslist(a[i]) + aslist(b[i])) == 0:
            continue
        if compare(a[i], b[i]):
            return True
        if compare(b[i], a[i]):
            return False

    return len(b) >= len(a)


def run(data):
    data = [json_loads(row) for row in data if row != ""]

    p1 = sum(i//2+1 for i in range(0, len(data), 2)
             if compare(data[i], data[i+1]))

    def _compare(a, b):
        if compare(a, b):
            return -1
        return 1

    _2, _6 = [[2]], [[6]]
    data += [_2, _6]
    data.sort(key=cmp_to_key(_compare))
    for i in range(len(data)):
        if data[i] == _2:
            p2 = i+1
        elif data[i] == _6:
            p2 *= i+1
            break

    return p1, p2
