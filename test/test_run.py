from d01.d01 import Day01
from d02.d02 import Day02
from d03.d03 import Day03
from d04.d04 import Day04
from d05.d05 import Day05
from d06.d06 import Day06
from d17.d17 import Day17

import time

EXPECTED_RESULTS = {
    "01": ("1319616", "27267728"),
    "02": ("213", "285"),
    "03": ("unknown", "unknown"),
    "04": ("unknown", "unknown"),
    "05": ("unknown", "unknown"),
    "06": ("unknown", "unknown"),
    "07": ("unknown", "unknown"),
    "08": ("unknown", "unknown"),
    "09": ("unknown", "unknown"),
    "10": ("unknown", "unknown"),
    "11": ("unknown", "unknown"),
    "12": ("unknown", "unknown"),
    "13": ("unknown", "unknown"),
    "14": ("unknown", "unknown"),
    "15": ("unknown", "unknown"),
    "16": ("unknown", "unknown"),
    "17": ("4,6,1,4,2,1,3,1,6", 'unknown'),
    "18": ("unknown", "unknown"),
    "19": ("unknown", "unknown"),
    "20": ("unknown", "unknown"),
    "21": ("unknown", "unknown"),
    "22": ("unknown", "unknown"),
    "23": ("unknown", "unknown"),
    "24": ("unknown", "unknown"),
    "25": ("unknown", "unknown"),
}

# Expected to pass a class with a .solve method that returns a tuple of strings
def runner(d, expected: tuple[str, str]):
    print()
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

def test_Day03():
    d = Day03()
    runner(d, EXPECTED_RESULTS['03'])

def test_Day04():
    d = Day04()
    runner(d, EXPECTED_RESULTS['04'])

def test_Day05():
    d = Day05()
    runner(d, EXPECTED_RESULTS['05'])

# def test_Day06():
#     d = Day06()
#     runner(d, EXPECTED_RESULTS['06'])

def test_Day17():
    d = Day17()
    runner(d, EXPECTED_RESULTS['17'])
