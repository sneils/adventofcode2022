from importlib import import_module
from pathlib import Path


def run(day, input_path):
    data_path = "{}/{}/{}.txt".format(
        Path(__file__).parent.parent.resolve(), input_path, day)

    with open(data_path) as f:
        data = f.readlines()

    return import_module(f"solutions.{day}").run(data)
