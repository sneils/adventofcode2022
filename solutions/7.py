from pprint import pprint


def run(data):
    fs = {"/": 0}
    wd = []

    for line in data:
        line = line.rstrip().split(" ")

        if line[0] == "$":
            match line[1]:
                case "cd":
                    if line[2] == "/":
                        continue
                    elif line[2] == "..":
                        wd.pop()
                    else:
                        wd.append(line[2])
                        fs["/" + "/".join(wd)] = 0
                case "ls":
                    continue
                case _:
                    raise ValueError
        elif line[0] == "dir":
            continue
        else:
            fs["/" + "/".join(wd)] += int(line[0])

    sizes = {}
    for dir in fs.keys():
        sizes[dir] = fs[dir] + sum(s for d, s in fs.items()
                                   if d != dir and d.startswith(dir.rstrip("/") + "/"))

    p1 = sum(s for s in sizes.values() if s <= 100_000)

    total = 70_000_000
    needs = 30_000_000

    for s in sorted(sizes.values()):
        if total - sizes["/"] + s >= needs:
            p2 = s
            break

    return p1, p2
