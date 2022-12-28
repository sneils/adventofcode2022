from math import prod


class Troop:
    def __init__(self):
        self.monkeys = []
        self.reduce_worry = lambda x: x // 3

    def add(self, monkey):
        self.monkeys.append(monkey)

    def play(self, rounds, reduce_worry=True):
        lcm = prod([m.test_divisor for m in self.monkeys])
        for _ in range(rounds):
            for i in range(len(self.monkeys)):
                for (i, item) in self.monkeys[i].handle_items(lcm, reduce_worry):
                    self.monkeys[i].add_item(item)

    def calc_monkey_business(self):
        (a, b) = sorted([m.inspected for m in self.monkeys])[-2:]
        return a * b


class Monkey:
    def __init__(
        self, items, operation, operation_with, test_divisor, test_true, test_false
    ):
        self.items = items
        self.operation = operation
        self.operation_with = operation_with
        self.test_divisor = test_divisor
        self.test_true = test_true
        self.test_false = test_false
        self.inspected = 0

    def handle_items(self, lcm, reduce_worry=True):
        moved = []
        for i in range(len(self.items)):
            if self.operation_with == "old":
                n = self.items[i]
            else:
                n = int(self.operation_with)
            match self.operation:
                case "+":
                    self.items[i] += n
                case "*":
                    self.items[i] *= n
                case _:
                    raise ValueError

            if reduce_worry:
                self.items[i] //= 3

            self.items[i] %= lcm

            if self.items[i] % self.test_divisor == 0:
                moved.append((self.test_true, self.items[i]))
            else:
                moved.append((self.test_false, self.items[i]))
            self.inspected += 1

        self.items.clear()
        return moved

    def add_item(self, worry_level):
        self.items.append(worry_level)


def parse_troop(data):
    def parse_monkey(data):
        return Monkey(
            [int(item) for item in data[1].split(": ")[1].split(", ")],
            data[2].split()[-2],
            data[2].split()[-1],
            int(data[3].split()[-1]),
            int(data[4].split()[-1]),
            int(data[5].split()[-1]),
        )

    troop = Troop()
    tmp = []
    for line in data:
        if line == "":
            troop.add(parse_monkey(tmp))
            tmp.clear()
            continue

        tmp.append(line)

    troop.add(parse_monkey(tmp))
    return troop


def run(data, args):
    troop1 = parse_troop(data)
    troop1.play(20)

    troop2 = parse_troop(data)
    troop2.play(10_000, False)

    return troop1.calc_monkey_business(), troop2.calc_monkey_business()
