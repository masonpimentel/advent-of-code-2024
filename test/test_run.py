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
from d15.d15 import Day15
from d16.d16 import Day16
from d17.d17 import Day17
from d18.d18 import Day18
from d19.d19 import Day19
from d20.d20 import Day20
from d21.d21 import Day21
from d22.d22 import Day22
from d23.d23 import Day23
from d24.d24 import Day24
from d25.d25 import Day25

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
    "16": ("135536", "583"),
    "17": ("4,6,1,4,2,1,3,1,6", "202366627359274"),
    "18": ("324", "46,23"),
    "19": ("283", "615388132411142"),
    "20": ("1426", "1000697"),
    "21": ("164960", "205620604017764"),
    "22": ("14082561342", "1568"),
    "23": ("1476", "ca,dw,fo,if,ji,kg,ks,oe,ov,sb,ud,vr,xr"),
    "24": ("57632654722854", "ckj,dbp,fdv,kdf,rpp,z15,z23,z39"),
    "25": ("3223", "NO_PT_2"),
}

def runner(d, day_str: str):
    print(f"\nRunning Day {day_str}")
    expected = EXPECTED_RESULTS[day_str]
    start = time.perf_counter()

    res = d.solve()
    assert res[0] == expected[0]
    assert res[1] == expected[1]
    print(f"pt_1_res: {res[0]}")
    print(f"pt_2_res: {res[1]}")

    end = time.perf_counter()
    s = end - start
    print(f"Elapsed {s:.03f} seconds")


def test_Day01():
    d = Day01()
    s = "01"
    runner(d, s)


def test_Day02():
    d = Day02()
    s = "02"
    runner(d, s)


def test_Day03():
    d = Day03()
    s = "03"
    runner(d, s)


def test_Day04():
    d = Day04()
    s = "04"
    runner(d, s)


def test_Day05():
    d = Day05()
    s = "05"
    runner(d, s)


def test_Day06():
    d = Day06()
    s = "06"
    runner(d, s)


def test_Day07():
    d = Day07()
    s = "07"
    runner(d, s)


def test_Day08():
    d = Day08()
    s = "08"
    runner(d, s)


def test_Day09():
    d = Day09()
    s = "09"
    runner(d, s)


def test_Day10():
    d = Day10()
    s = "10"
    runner(d, s)


def test_Day11():
    d = Day11()
    s = "11"
    runner(d, s)


def test_Day12():
    d = Day12()
    s = "12"
    runner(d, s)


def test_Day13():
    d = Day13()
    s = "13"
    runner(d, s)


def test_Day14():
    d = Day14()
    s = "14"
    runner(d, s)


def test_Day15():
    d = Day15()
    s = "15"
    runner(d, s)


def test_Day16():
    d = Day16()
    s = "16"
    runner(d, s)


def test_Day17():
    d = Day17()
    s = "17"
    runner(d, s)


def test_Day18():
    d = Day18()
    s = "18"
    runner(d, s)


def test_Day19():
    d = Day19()
    s = "19"
    runner(d, s)


def test_Day20():
    d = Day20()
    s = "20"
    runner(d, s)


def test_Day21():
    d = Day21()
    s = "21"
    runner(d, s)


def test_Day22():
    d = Day22()
    s = "22"
    runner(d, s)


def test_Day23():
    d = Day23()
    s = "23"
    runner(d, s)


def test_Day24():
    d = Day24()
    s = "24"
    runner(d, s)


def test_Day25():
    d = Day25()
    s = "25"
    runner(d, s)
