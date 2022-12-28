from solutions import run_sample, run_puzzle
from time import time
from argparse import ArgumentParser, BooleanOptionalAction

if __name__ == "__main__":
    parser = ArgumentParser(prog="adventofcode2022")
    parser.add_argument("-d", "--day", type=int)
    parser.add_argument("-s", "--use-sample", action=BooleanOptionalAction)
    parser.add_argument("optionals", nargs="*")
    args = parser.parse_args().__dict__

    a, b = 1, 25
    if args["day"] != None:
        a, b = args["day"], args["day"]

    for day in range(a, b + 1):
        start = time()
        try:
            if args["use_sample"]:
                results = run_sample(day, args)
            else:
                results = run_puzzle(day, args)

            print(day, results, round(time() - start, 2), "s")

        except FileNotFoundError:
            print(day, "input file not found :(")
            break

        except ModuleNotFoundError:
            print(day, "not yet implemented :(")
            break
