from json import loads as json_loads
from functools import cmp_to_key


def compare(a, b):
    def _list(x):
        return x if isinstance(x, list) else [x]

    if type(a) != type(b):
        return compare(_list(a), _list(b))

    if isinstance(a, int):
        return a < b

    for i in range(min(len(a), len(b))):
        if len(_list(a[i]) + _list(b[i])) == 0:
            continue
        if compare(a[i], b[i]):
            return True
        if compare(b[i], a[i]):
            return False

    return len(b) >= len(a)


def run(data, args):
    data = [json_loads(row) for row in data if row != ""]

    p1 = sum(
        i // 2 + 1 for i in range(0, len(data), 2) if compare(data[i], data[i + 1])
    )

    _2, _6 = [[2]], [[6]]
    data += [_2, _6]
    data.sort(key=cmp_to_key(lambda a, b: -1 if compare(a, b) else 1))
    for i in range(len(data)):
        if data[i] == _2:
            p2 = i + 1
        elif data[i] == _6:
            p2 *= i + 1
            break

    return p1, p2
