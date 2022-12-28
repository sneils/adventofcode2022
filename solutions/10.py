class CPU:
    def __init__(self):
        self.x = 1
        self.xs = []
        self.cycle = 0

    def run(self, instructions):
        for instruction in instructions:
            self.cycle += 1
            self.learn()
            self.draw()

            if instruction == "noop":
                continue

            _, n = self.parse(instruction)
            self.cycle += 1
            self.learn()
            self.draw()
            self.x += n

    def parse(self, instruction):
        return [t(s) for t, s in zip((str, int), instruction.split())]

    def draw(self):
        m = self.cycle % 40 - 1
        if self.x in [m - 1, m, m + 1]:
            print("#", end="")
        else:
            print(".", end="")
        if self.cycle % 40 == 0:
            print()

    def learn(self):
        if self.cycle == 20 or self.cycle % 40 == 20:
            self.xs.append(self.cycle * self.x)

    def learned(self):
        return sum(self.xs)


def run(data):
    cpu = CPU()
    cpu.run(data)
    return cpu.learned(), 0
