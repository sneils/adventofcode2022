class Cave:
    def __init__(self, rocks, has_floor=False, start=(500, 0)):
        self.has_floor = has_floor
        self.start = start
        self.rocks = set(rocks)
        self.sand = set()
        self.minmax()

        if self.has_floor:
            n = 2
            h = self.max[1] - self.min[1] + n
            for x in range(self.start[0] - h, self.start[0] + h + 1):
                self.rocks.add((x, self.max[1] + n))
            self.minmax()

    def minmax(self):
        xs = [r[0] for r in self.rocks] + [self.start[0]]
        ys = [r[1] for r in self.rocks] + [self.start[1]]
        self.min = (min(xs), min(ys))
        self.max = (max(xs), max(ys))
        self.valid_x = list(range(self.min[0], self.max[0] + 1))
        self.valid_y = list(range(self.min[1], self.max[1] + 1))

    def is_oob(self, point):
        return point[0] not in self.valid_x or point[1] not in self.valid_y

    def is_free(self, point):
        return point not in self.rocks | self.sand

    def drop_down(self, point):
        down = (point[0], point[1] + 1)
        while self.is_free(down):
            if self.is_oob(down):
                raise IndexError
            point = down
            down = (point[0], point[1] + 1)
        return point

    def flow_next(self, point):
        left = (point[0] - 1, point[1] + 1)
        if self.is_free(left):
            return self.drop_down(left)
        right = (point[0] + 1, point[1] + 1)
        if self.is_free(right):
            return self.drop_down(right)
        return None

    def prefill(self):
        for y in range(1, self.max[1]):
            for x in range(self.start[0] - y, self.start[0] + y + 1):
                if y != 1 and not any(
                    point in self.sand
                    for point in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
                ):
                    continue

                point = (x, y)
                if self.is_free(point):
                    self.sand.add(point)

    def overflow(self, progress=False):
        if self.has_floor:
            self.prefill()

        if progress:
            self.print()

        try:
            while True:
                point = self.drop_down(self.start)
                next = self.flow_next(point)
                while next != None:
                    point = next
                    next = self.flow_next(point)

                self.sand.add(point)
                if progress:
                    self.print()

                if self.start == point:
                    raise IndexError

        except IndexError:
            pass

    def print(self):
        yw = len(str(self.max[1]))
        w = self.max[0] - self.min[0] + 1 + yw + 1
        print("=" * w)
        for y in range(self.min[1], self.max[1] + 1):
            print(str(y).ljust(yw), end=" ")
            for x in range(self.min[0], self.max[0] + 1):
                p = (x, y)
                if p == self.start:
                    print("+", end="")
                elif p in self.sand:
                    print("o", end="")
                elif p in self.rocks:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print("=" * w)


def run(data, args):
    def _point(input):
        x, y = input.split(",")
        return (int(x), int(y))

    def _rocks(formation):
        def _range(a, b):
            if a[0] == b[0]:
                return ((a[0], y) for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1))
            return ((x, a[1]) for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1))

        rocks = []
        a = formation[0]
        for i in range(len(formation) - 1):
            b = formation[i + 1]
            rocks += _range(a, b)
            a = b

        return rocks

    def _formation(input):
        return _rocks([_point(p) for p in input.split(" -> ")])

    rocks = sum([_formation(row) for row in data], [])

    cave = Cave(rocks)
    cave.overflow()
    p1 = len(cave.sand)

    cave = Cave(rocks, has_floor=True)
    cave.overflow()
    p2 = len(cave.sand)

    return p1, p2
