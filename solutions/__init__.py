from importlib import import_module
from pathlib import Path


def get_input(path):
    input_path = "{}/{}".format(
        Path(__file__).parent.parent.resolve(), path)

    with open(input_path) as f:
        return f.readlines()


def run_puzzle(day):
    return run(day, get_input(f"puzzles/{day}.txt"))


def run_sample(day, suffix=""):
    return run(day, get_input(f"samples/{day}{suffix}.txt"))


def run(day, data):
    return import_module(f"solutions.{day}").run(data)
