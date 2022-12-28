from importlib import import_module
from pathlib import Path
from typing import Tuple


def get_input(path):  # -> list[str]:
    return Path("{}/../{}".format(__path__[0], path)).read_text().splitlines()
    # TODO: should we stream instead? might need to change some solutions in this case
    # with open(input_path) as f:
    #   for line in f:
    #       yield line.rstrip()


def run_puzzle(day):  # -> Tuple[int | str, int | str]:
    return run(day, get_input(f"puzzles/{day}.txt"))


def run_sample(day, suffix=""):  # -> Tuple[int | str, int | str]:
    return run(day, get_input(f"samples/{day}{suffix}.txt"))


def run(day, data):  # -> Tuple[int | str, int | str]:
    return import_module(f"solutions.{day}").run(data)
