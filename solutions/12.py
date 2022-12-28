from collections import deque


def get_neighbors(data, pos):
    n, (x, y) = [], pos

    if y > 0:
        n.append((x, y - 1))
    if y < len(data) - 1:
        n.append((x, y + 1))
    if x > 0:
        n.append((x - 1, y))
    if x < len(data[y]) - 1:
        n.append((x + 1, y))

    return [(nx, ny) for (nx, ny) in n if ord(data[ny][nx]) <= ord(data[y][x]) + 1]


def find_route(data, pos, goal):
    seen = set()
    moves = deque([(pos, 0)])

    while moves:
        check, steps = moves.popleft()

        if check == goal:
            return steps

        if check in seen:
            continue

        seen.add(check)
        moves += [(n, steps + 1) for n in get_neighbors(data, check)]


def run(data):
    todo_p2 = []

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "a":
                todo_p2.append((x, y))
            elif data[y][x] == "S":
                pos = (x, y)
                data[y] = data[y].replace("S", "a")
            elif data[y][x] == "E":
                goal = (x, y)
                data[y] = data[y].replace("E", "z")

    p1 = find_route(data, pos, goal)
    p2 = min(
        filter(lambda n: n != None, (find_route(data, pos, goal) for pos in todo_p2))
    )

    return p1, p2
