from importlib import import_module
from pathlib import Path


def get_input(path):
    return Path("{}/../{}".format(__path__[0], path)).read_text().splitlines()
    # TODO: should we stream instead? might need to change some solutions in this case
    # with open(input_path) as f:
    #   for line in f:
    #       yield line.rstrip()


def run_puzzle(day, args={}):
    return run(day, get_input(f"puzzles/{day}.txt"), {"use_sample": False} | args)


def run_sample(day, args={}):
    return run(day, get_input(f"samples/{day}.txt"), {"use_sample": True} | args)


def run(day, data, args={}):
    return import_module(f"solutions.{day}").run(data, {"day": day} | args)
