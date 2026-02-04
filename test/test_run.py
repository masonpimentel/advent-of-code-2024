from solvers.d01.d01 import Day01
from solvers.d02.d02 import Day02
from solvers.d03.d03 import Day03
from solvers.d04.d04 import Day04
from solvers.d05.d05 import Day05
from solvers.d06.d06 import Day06
from solvers.d07.d07 import Day07
from solvers.d08.d08 import Day08
from solvers.d09.d09 import Day09
from solvers.d10.d10 import Day10
from solvers.d11.d11 import Day11
from solvers.d12.d12 import Day12
from solvers.d13.d13 import Day13
from solvers.d14.d14 import Day14
from solvers.d15.d15 import Day15
from solvers.d16.d16 import Day16
from solvers.d17.d17 import Day17
from solvers.d18.d18 import Day18
from solvers.d19.d19 import Day19
from solvers.d20.d20 import Day20
from solvers.d21.d21 import Day21
from solvers.d22.d22 import Day22
from solvers.d23.d23 import Day23
from solvers.d24.d24 import Day24
from solvers.d25.d25 import Day25

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


def do_run(d, expected: str, times: list[float]):
    start = time.perf_counter()
    res = d.solve()
    end = time.perf_counter()

    assert res[0] == expected[0]
    assert res[1] == expected[1]

    elapsed = end - start
    times.append(elapsed)

    return res


def runner(d, day_str: str, runs: int = 1):
    print(f"\nRunning Day {day_str}")
    expected = EXPECTED_RESULTS[day_str]

    # Warm-up
    d.solve()

    times = []
    if runs == 1:
        res = do_run(d, expected, times)
        print(f"Elapsed {times[-1]:.03f} seconds")
    else:
        for i in range(runs):
            res = do_run(d, expected, times)
            print(f"Run {i + 1}: {times[-1]:.03f}s")

        avg = sum(times) / runs
        print(f"Average over {runs} runs: {avg:.03f}s")

    print(f"pt_1_res: {res[0]}")
    print(f"pt_2_res: {res[1]}")


def test_Day01(runs):
    runner(Day01(), "01", runs)


def test_Day02(runs):
    runner(Day02(), "02", runs)


def test_Day03(runs):
    runner(Day03(), "03", runs)


def test_Day04(runs):
    runner(Day04(), "04", runs)


def test_Day05(runs):
    runner(Day05(), "05", runs)


def test_Day06(runs):
    runner(Day06(), "06", runs)


def test_Day07(runs):
    runner(Day07(), "07", runs)


def test_Day08(runs):
    runner(Day08(), "08", runs)


def test_Day09(runs):
    runner(Day09(), "09", runs)


def test_Day10(runs):
    runner(Day10(), "10", runs)


def test_Day11(runs):
    runner(Day11(), "11", runs)


def test_Day12(runs):
    runner(Day12(), "12", runs)


def test_Day13(runs):
    runner(Day13(), "13", runs)


def test_Day14(runs):
    runner(Day14(), "14", runs)


def test_Day15(runs):
    runner(Day15(), "15", runs)


def test_Day16(runs):
    runner(Day16(), "16", runs)


def test_Day17(runs):
    runner(Day17(), "17", runs)


def test_Day18(runs):
    runner(Day18(), "18", runs)


def test_Day19(runs):
    runner(Day19(), "19", runs)


def test_Day20(runs):
    runner(Day20(), "20", runs)


def test_Day21(runs):
    runner(Day21(), "21", runs)


def test_Day22(runs):
    runner(Day22(), "22", runs)


def test_Day23(runs):
    runner(Day23(), "23", runs)


def test_Day24(runs):
    runner(Day24(), "24", runs)


def test_Day25(runs):
    runner(Day25(), "25", runs)
