from d01.d01 import Day01
from d02.d02 import Day02
from d17.d17 import Day17

import time

EXPECTED_RESULTS = {
    "01": ("1319616", "27267728"),
    "02": ("213", "285"),
    "17": ("4,6,1,4,2,1,3,1,6", 'unknown')
}

# Expected to pass a class with a .solve method that returns a tuple of strings
def runner(d, expected: tuple[str, str]):
    start = time.perf_counter()

    res = d.solve()
    assert res[0] == expected[0]
    assert res[1] == expected[1]

    end = time.perf_counter()
    s = (end-start)
    print(f"Elapsed {s:.03f} seconds")


def test_Day01():
    d = Day01()
    runner(d, EXPECTED_RESULTS['01'])

def test_Day02():
    d = Day02()
    runner(d, EXPECTED_RESULTS['02'])

def test_Day17():
    d = Day17()
    runner(d, EXPECTED_RESULTS['17'])
