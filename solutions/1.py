def run(data, args):
    elves = []
    cur = 0
    for line in data:
        if line == "":
            elves.append(cur)
            cur = 0
        else:
            cur += int(line)

    elves.append(cur)
    elves.sort()

    return sum(elves[-1:]), sum(elves[-3:])
