from solutions import run
from sys import argv
from time import time

if __name__ == "__main__":
    a, b = 1, 25
    if len(argv) > 1:
        a, b = int(argv[1]), int(argv[1])

    for day in range(a, b+1):
        start = time()
        try:
            print(day, run(day, "puzzles"), round(time()-start, 2), "s")

        except FileNotFoundError:
            print(day, "input file not found :(")
            break

        except ModuleNotFoundError:
            print(day, "not yet implemented :(")
            break
