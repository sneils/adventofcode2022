from re import compile as re_compile


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def y_range(sensor, beacon, y):
    d = dist(sensor, beacon)
    return set(
        x for x in range(sensor[0] - d, sensor[0] + d + 1) if dist(sensor, (x, y)) <= d
    )


def in_range(links, p):
    for sensor, beacon in links.items():
        if dist(sensor, p) <= dist(sensor, beacon):
            return True
    return False


def perimeter(sensor, beacon, d_max):
    def x(y):
        return sx + xd * d + xy * (y - sy)

    sx, sy = sensor
    d, p = dist(sensor, beacon) + 1, set()
    q = [
        (-1, -1, -d, +0),  # x=-d,y=+0 => x=+0,y=-d -> 9-12
        (+1, +1, -d, +0),  # x=+0,y=-d => x=+d,y=+0 -> 0-3
        (+1, -1, -0, +d),  # x=+d,y=+0 => x=+0,y=+d -> 3-6
        (-1, +1, -0, +d),  # x=+0,y=+d => x=-d,y=+0 -> 6-9
    ]
    for (xd, xy, ya, yb) in q:
        p |= set(
            (x(y), y)
            for y in range(max(0, sy + ya), min(d_max, sy + yb) + 1)
            if 0 <= x(y) <= d_max
        )
    return p


def find_blindspot(links, d_max):
    for sensor, beacon in links.items():
        for p in perimeter(sensor, beacon, d_max):
            if in_range(links, p):
                continue
            return p


def draw(links, d_max, marks=set()):
    def _coverage(sensor, beacon):
        d = dist(sensor, beacon)
        c = set()
        for y in range(sensor[1] - d, sensor[1] + d + 1):
            for x in range(sensor[0] - d, sensor[0] + d + 1):
                p = (x, y)
                if dist(sensor, p) <= d:
                    c.add(p)
        return c

    beacons = set(links.values())
    sensors = set(links.keys())
    covered = marks

    if len(marks) == 0:
        for sensor, beacon in links.items():
            covered |= _coverage(sensor, beacon)

    distress = set()
    for y in range(d_max + 1):
        for x in range(d_max + 1):
            distress.add((x, y))

    xs = [c[0] for c in sensors | beacons | covered]
    ys = [c[1] for c in sensors | beacons | covered]

    xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)

    wy = max(len(str(ymin)), len(str(ymax)))
    w = wy + 1 + xmax - xmin + 1

    print(xmin, xmax)

    print("=" * w)
    print("{} {}0".format(" " * wy, " " * abs(xmin)))
    for y in range(ymin, ymax + 1):
        print(str(y).ljust(wy), end=" ")
        for x in range(xmin, xmax + 1):
            p = (x, y)
            if p in sensors:
                print("S", end="")
            elif p in beacons:
                print("B", end="")
            elif p in covered:
                print("#", end="")
            elif p in distress:
                print(".", end="")
            else:
                print(".", end="")
        print()
    print("{} {}0".format(" " * wy, " " * abs(xmin)))
    print("=" * w)


def run(data, args):
    y_check = 10 if args["use_sample"] else 2_000_000

    RE = re_compile(
        r"^Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)$"
    )

    links, covered = dict(), set()
    for row in data:
        sx, sy, bx, by = (int(x) for x in RE.match(row).groups())
        sensor, beacon = (sx, sy), (bx, by)
        links[sensor] = beacon
        covered |= (
            y_range(sensor, beacon, y_check)
            .difference(x for (x, y) in links.keys() if y == y_check)
            .difference(x for (x, y) in links.values() if y == y_check)
        )
    p1 = len(covered)

    x_multi = 4_000_000
    (bx, by) = find_blindspot(links, 2 * y_check)
    p2 = bx * x_multi + by

    return p1, p2
