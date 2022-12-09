class Knot:
    def __init__(self):
        self.x, self.y = 0, 0
        self.visits = set()
        self.visit()

    def get(self):
        return self.x, self.y

    def visit(self):
        self.visits.add("{},{}".format(self.x, self.y))

    def visited(self, x, y):
        return "{},{}".format(x, y) in self.visits

    def move(self, direction):
        match direction:
            case "L":
                self.x -= 1
            case "R":
                self.x += 1
            case "U":
                self.y += 1
            case "D":
                self.y -= 1
            case _:
                raise ValueError

        self.visit()

    def pull(self, to):
        dx, dy = to.x-self.x, to.y-self.y
        if abs(dx) > 1 or abs(dy) > 1:
            self.x += max(-1, min(1, dx))
            self.y += max(-1, min(1, dy))

        self.visit()


class Rope:
    def __init__(self, n):
        self.parts = [Knot() for _ in range(n)]

    def head(self):
        return self.parts[0]

    def tail(self):
        return self.parts[-1]

    def move(self, direction, distance):
        for _ in range(distance):
            self.head().move(direction)
            self.pull()

    def pull(self):
        for i in range(1, len(self.parts)):
            last, curr = self.parts[i-1:i+1]
            curr.pull(last)


def parse(line):
    return [t(s) for t, s in zip((str, int), line.split())]


def print(rope, mark_path=False):
    d = 5  # d=200
    for y in range(d, -d-1, -1):
        for x in range(-d, d+1, +1):
            if (x, y) == rope.head().get():
                print("H", end="")
            elif (x, y) == rope.tail().get():
                print("T", end="")
            elif (x, y) == (0, 0):
                print("s", end="")
            elif mark_path and rope.tail().visited(x, y):
                print("x", end="")
            else:
                print(".", end="")

        print()

    print()


def run(data):
    rope = Rope(2)

    for line in data:
        d, n = parse(line)
        rope.move(d, n)

    return len(rope.tail().visits), 0
