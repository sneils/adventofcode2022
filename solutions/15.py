from re import compile as re_compile
from time import time
from functools import reduce


def tt(s, t):
    print(s, round(time() - t, 2))


def scan_y(sensors, y):
    todo = [sensor for sensor in sensors if sensor.sy + sensor.d >= y]
    xmin = min([sensor.sx - sensor.d // 2 for sensor in todo])
    xmax = max([sensor.sx + sensor.d // 2 for sensor in todo])
    used = len(set([sensor.bx for sensor in todo if sensor.by == y]))
    return sum(1 for x in range(xmin, xmax + 1) if in_range(todo, (x, y))) - used


def in_range(sensors, p):
    t = time()
    x, y = p
    for sensor in sensors:
        if sensor.dist(x, y) <= sensor.d:
            # print("in_range", sensor, x, y, True, round(time() - t, 2))
            return True
    # print("in_range", sensor, x, y, False, round(time() - t, 2))
    return False


def perimeter(sensor, d_max):
    t = time()

    def x(y):
        return _x + xy * (y - sensor.sy)

    p = []
    q = [
        (-1, -1, -sensor.d - 1, +0),  # x=-d,y=+0 => x=+0,y=-d -> 9-12
        (+1, +1, -sensor.d - 1, +0),  # x=+0,y=-d => x=+d,y=+0 -> 0-3
        (+1, -1, -0, +sensor.d + 1),  # x=+d,y=+0 => x=+0,y=+d -> 3-6
        (-1, +1, -0, +sensor.d + 1),  # x=+0,y=+d => x=-d,y=+0 -> 6-9
    ]
    for (xd, xy, ya, yb) in q:
        _x = sensor.sx + xd * sensor.d + 1
        p += [
            (x(y), y)
            for y in range(max(0, sensor.sy + ya), min(d_max, sensor.sy + yb) + 1)
            if 0 <= x(y) <= d_max
        ]
    print("perimeter", sensor, round(time() - t, 2))
    return p


def find_blindspot(sensors, d_max):
    IN_RANGE_TIME = {sensor: 0 for sensor in sensors}
    CHECKS_NEEDED = {sensor: 0 for sensor in sensors}
    for sensor in sensors:
        for p in perimeter(sensor, d_max):
            t = time()
            if in_range(sensors, p):
                CHECKS_NEEDED[sensor] += 1
                IN_RANGE_TIME[sensor] += time() - t
                continue

            # pprint(CHECKS_NEEDED)
            # pprint(IN_RANGE_TIME)
            return p


class Sensor:
    def __init__(self, sx, sy, bx, by):
        self.sx, self.sy, self.bx, self.by = sx, sy, bx, by
        self.d = self.dist(bx, by)

    def dist(self, x, y):
        return abs(self.sx - x) + abs(self.sy - y)

    def __repr__(self):
        return str((self.sx, self.sy))


def run(data, args):
    y = 10 if args["use_sample"] else 2_000_000

    RE = re_compile(
        r"^Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)$"
    )

    def _parse(row):
        sx, sy, bx, by = (int(x) for x in RE.match(row).groups())
        return Sensor(sx, sy, bx, by)

    sensors = [_parse(row) for row in data]
    t = time()
    p1 = scan_y(sensors, y)
    print(round(time() - t, 2))

    x_multi = 4_000_000
    (bx, by) = find_blindspot(sensors, 2 * y)
    p2 = bx * x_multi + by

    return p1, p2
