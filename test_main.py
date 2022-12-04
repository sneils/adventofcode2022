import pytest
from solutions import run

SAMPLES = [
    (1, 24000, 45000),
    (2, 15, 12),
    (3, 157, 70),
    (4, 2, 4),
]


@pytest.mark.parametrize('day,part1,part2', SAMPLES)
def test_urls(day, part1, part2):
    assert (part1, part2) == run(day, "samples")
