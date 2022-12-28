def find_marker(stream, n):
    for i in range(len(stream) - n + 1):
        if len(set(stream[i : i + n])) == n:
            return i + n

    raise LookupError


def run(data):
    return find_marker(data[0], 4), find_marker(data[0], 14)
