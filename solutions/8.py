from math import prod


def left(x, y, data):
    return data[y][:x][::-1]


def right(x, y, data):
    return data[y][x + 1 :]


def up(x, y, data):
    return [data[i][x] for i in range(len(data)) if i < y][::-1]


def down(x, y, data):
    return [data[i][x] for i in range(len(data)) if i > y]


def is_visible(x, y, data):
    return any(
        data[y][x] > tree
        for tree in [
            max(left(x, y, data)),
            max(right(x, y, data)),
            max(up(x, y, data)),
            max(down(x, y, data)),
        ]
    )


def get_score(x, y, data):
    def _(tree, trees):
        score = 0
        for h in trees:
            score += 1
            if h >= tree:
                break
        return score

    return prod(
        [
            _(data[y][x], left(x, y, data)),
            _(data[y][x], right(x, y, data)),
            _(data[y][x], up(x, y, data)),
            _(data[y][x], down(x, y, data)),
        ]
    )


def run(data):
    p1 = 2 * (len(data) + len(data[0])) - 4
    p2 = 0

    for y in range(1, len(data) - 1):
        for x in range(1, len(data[y]) - 1):
            p1 += int(is_visible(x, y, data))
            p2 = max(p2, get_score(x, y, data))

    return p1, p2
