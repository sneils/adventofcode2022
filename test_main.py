import pytest
from solutions import run_sample, run

SAMPLES = [
    (1, 24000, 45000),
    (2, 15, 12),
    (3, 157, 70),
    (4, 2, 4),
    (5, "CMZ", "MCD"),
    (7, 95437, 24933642),
    (8, 21, 8),
]


@pytest.mark.parametrize('day,part1,part2', SAMPLES)
def test_samples(day, part1, part2):
    assert (part1, part2) == run_sample(day)


SAMPLES_6 = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26),
]


@pytest.mark.parametrize('input,part1,part2', SAMPLES_6)
def test_6(input, part1, part2):
    assert (part1, part2) == run(6, [input])
