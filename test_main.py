import pytest
from solutions import run_sample

SAMPLES = [
    (1, 24000, 45000),
    (2, 15, 12),
    (3, 157, 70),
    (4, 2, 4),
    (5, "CMZ", -1),
]


@pytest.mark.parametrize('day,part1,part2', SAMPLES)
def test_samples(day, part1, part2):
    assert (part1, part2) == run_sample(day)
