from re import compile as re_compile


class StackMover:
    MOVE_REGEX = re_compile(r"^move ([0-9]+) from ([0-9]+) to ([0-9]+)")

    def __init__(self, version):
        self.version = version
        self.stacks = []

    def add(self, stack, crate):
        while len(self.stacks) <= stack:
            self.stacks.append("")
        self.stacks[stack] += crate

    def move(self, move):
        n, a, b = (int(x) for x in self.MOVE_REGEX.match(move).groups())

        match self.version:
            case 9000:
                self.stacks[b - 1] += self.stacks[a - 1][-n:][::-1]
            case 9001:
                self.stacks[b - 1] += self.stacks[a - 1][-n:]
            case _:
                raise ValueError

        self.stacks[a - 1] = self.stacks[a - 1][:-n]

    def top(self):
        return "".join(x[-1] for x in self.stacks if len(x) > 0)


def run(data):
    stacks = (StackMover(9000), StackMover(9001))

    for line in reversed(data):
        if line.find("[") < 0:
            continue

        for i in range(0, len(line), 4):
            if line[i + 1] == " ":
                continue

            for stack in stacks:
                stack.add(i // 4, line[i + 1])

    for line in data:
        if not line.startswith("move"):
            continue

        for stack in stacks:
            stack.move(line)

    return stacks[0].top(), stacks[1].top()
