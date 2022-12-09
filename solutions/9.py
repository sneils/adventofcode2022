class Knot:
    def __init__(self):
        self.x, self.y = 0, 0
        self.next = None
        self.visits = set()
        self.visit()

#    def get(self):
#        return self.x, self.y
#
#    def visited(self, x, y):
#        return "{},{}".format(x, y) in self.visits

    def visit(self):
        self.visits.add("{},{}".format(self.x, self.y))

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
        self.pull()

    def pull(self):
        if self.next == None:
            return

        dx, dy = self.x-self.next.x, self.y-self.next.y
        if abs(dx) > 1 or abs(dy) > 1:
            self.next.x += max(-1, min(1, dx))
            self.next.y += max(-1, min(1, dy))

        self.next.pull()
        self.next.visit()


class Rope:
    def __init__(self, n):
        self.head = knot = Knot()
        for _ in range(1, n):
            knot.next = Knot()
            knot = knot.next
        self.tail = knot

    def move(self, direction, distance):
        for _ in range(distance):
            self.head.move(direction)


def parse(line):
    return [t(s) for t, s in zip((str, int), line.split())]


# def draw(rope, mark_path=False):
#    d = 5  # d=200
#    for y in range(d, -d-1, -1):
#        for x in range(-d, d+1, +1):
#            if (x, y) == rope.head.get():
#                print("H", end="")
#            elif (x, y) == rope.tail.get():
#                print("T", end="")
#            elif (x, y) == (0, 0):
#                print("s", end="")
#            elif mark_path and rope.tail.visited(x, y):
#                print("x", end="")
#            else:
#                print(".", end="")
#
#        print()
#
#    print()


def run(data):
    ropes = (Rope(2), Rope(10))

    for line in data:
        d, n = parse(line)
        for rope in ropes:
            rope.move(d, n)

    p1, p2 = [len(rope.tail.visits) for rope in ropes]
    return p1, p2
