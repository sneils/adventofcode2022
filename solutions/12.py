from collections import deque


def get_neighbors(M, pos):
    n, (x, y) = [], pos

    if y > 0:
        n.append((x, y-1))
    if y < len(M)-1:
        n.append((x, y+1))
    if x > 0:
        n.append((x-1, y))
    if x < len(M[y])-1:
        n.append((x+1, y))

    return [(nx, ny) for (nx, ny) in n if ord(M[ny][nx]) <= ord(M[y][x])+1]


def find_route(M, pos, goal):
    seen = set()
    moves = deque([(pos, 0)])

    while moves:
        check, steps = moves.popleft()

        if check == goal:
            return steps

        if check in seen:
            continue

        seen.add(check)
        moves += [(n, steps+1) for n in get_neighbors(M, check)]


def run(data):
    M = [list(line) for line in data]
    todo_p2 = []

    for y in range(len(M)):
        for x in range(len(M[y])):
            if M[y][x] == "a":
                todo_p2.append((x, y))
            elif M[y][x] == "S":
                pos = (x, y)
                M[y][x] = "a"
            elif M[y][x] == "E":
                goal = (x, y)
                M[y][x] = "z"

    p1 = find_route(M, pos, goal)
    p2 = min(filter(lambda n: n != None, (find_route(M, pos, goal)
             for pos in todo_p2)))

    return p1, p2
