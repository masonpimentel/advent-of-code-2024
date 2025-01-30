from d01.d01 import Day01

import time

EXPECTED_RESULTS = {
    '01': ('1319616', '27267728')
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