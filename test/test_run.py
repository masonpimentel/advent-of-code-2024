from d01.d01 import Day01
from d02.d02 import Day02
from d03.d03 import Day03
from d04.d04 import Day04
from d05.d05 import Day05
from d06.d06 import Day06
from d07.d07 import Day07
from d08.d08 import Day08
from d09.d09 import Day09
from d10.d10 import Day10
from d11.d11 import Day11
from d12.d12 import Day12
from d13.d13 import Day13
from d14.d14 import Day14
from d17.d17 import Day17

import time

EXPECTED_RESULTS = {
    "01": ("1319616", "27267728"),
    "02": ("213", "285"),
    "03": ("153469856", "77055967"),
    "04": ("2543", "1930"),
    "05": ("7074", "4828"),
    "06": ("5305", "2143"),
    "07": ("7885693428401", "348360680516005"),
    "08": ("311", "1115"),
    "09": ("6367087064415", "6390781891880"),
    "10": ("617", "1477"),
    "11": ("204022", "241651071960597"),
    "12": ("1437300", "849332"),
    "13": ("26599", "106228669504887"),
    "14": ("211692000", "6587"),
    "15": ("1514353", "1533076"),
    "16": ("1533076", "583"),
    "17": ("4,6,1,4,2,1,3,1,6", 'unknown'),
    "18": ("324", "46,23"),
    "19": ("283", "615388132411142"),
    "20": ("1426", "1000697"),
    "21": ("unknown", "unknown"),
    "22": ("unknown", "unknown"),
    "23": ("1476", "ca,dw,fo,if,ji,kg,ks,oe,ov,sb,ud,vr,xr"),
    "24": ("57632654722854", "unknown"),
    "25": ("3223", "unknown"),
}

# Expected to pass a class with a .solve method that returns a tuple of strings
def runner(d, expected: tuple[str, str], day_str: str):
    print()
    print(f'Running Day {day_str}')
    start = time.perf_counter()

    res = d.solve()
    assert res[0] == expected[0]
    assert res[1] == expected[1]

    end = time.perf_counter()
    s = (end-start)
    print(f"Elapsed {s:.03f} seconds")


def test_Day01():
    d = Day01()
    s = '01'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day02():
    d = Day02()
    s = '02'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day03():
    d = Day03()
    s = '03'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day04():
    d = Day04()
    s = '04'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day05():
    d = Day05()
    s = '05'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day06():
    d = Day06()
    s = '06'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day07():
    d = Day07()
    s = '07'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day08():
    d = Day08()
    s = '08'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day09():
    d = Day09()
    s = '09'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day10():
    d = Day10()
    s = '10'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day11():
    d = Day11()
    s = '11'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day12():
    d = Day12()
    s = '12'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day13():
    d = Day13()
    s = '13'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day14():
    d = Day14()
    s = '14'
    runner(d, EXPECTED_RESULTS[s], s)

def test_Day17():
    d = Day17()
    s = '17'
    runner(d, EXPECTED_RESULTS[s], s)
