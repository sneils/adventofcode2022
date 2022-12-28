def run(data):
    part1, part2 = 0, 0
    for line in data:
        a, b = line.split()
        match b:
            case "X":
                match a:
                    case "A":
                        part1 += 3 + 1
                        part2 += 0 + 3
                    case "B":
                        part1 += 0 + 1
                        part2 += 0 + 1
                    case "C":
                        part1 += 6 + 1
                        part2 += 0 + 2
                    case _:
                        raise ValueError
            case "Y":
                match a:
                    case "A":
                        part1 += 6 + 2
                        part2 += 3 + 1
                    case "B":
                        part1 += 3 + 2
                        part2 += 3 + 2
                    case "C":
                        part1 += 0 + 2
                        part2 += 3 + 3
                    case _:
                        raise ValueError
                pass
            case "Z":
                match a:
                    case "A":
                        part1 += 0 + 3
                        part2 += 6 + 2
                    case "B":
                        part1 += 6 + 3
                        part2 += 6 + 3
                    case "C":
                        part1 += 3 + 3
                        part2 += 6 + 1
                    case _:
                        raise ValueError
                pass
            case _:
                raise ValueError

    return part1, part2
