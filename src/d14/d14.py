from re import search
from base.day import Day

COLS = 101
ROWS = 103

HORIZ_WALL = ROWS // 2
VERT_WALL = COLS // 2

PT_2_UPPER = 10000

from os.path import join


class Day14(Day):
    def solve(self):
        pt_1_res = ""
        pt_2_res = ""

        with open(join("src", "d14", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            robots: list[list[int, int, int, int]] = []

            while line:
                # a = search(r'Button A: X\+(\d*), Y\+(\d*)', line)
                vals = search(r"p=(\d*),(\d*) v=(-?\d*),(-?\d*)", line)
                robots.append(
                    [
                        int(vals.group(1)),
                        int(vals.group(2)),
                        int(vals.group(3)),
                        int(vals.group(4)),
                    ]
                )

                line = f.readline()

            # print(robots)

            orig_robots = robots[:]

            l = len(robots)
            for time in range(100):
                for i in range(l):
                    robots[i][0] = robots[i][0] + robots[i][2]
                    robots[i][1] = robots[i][1] + robots[i][3]

                # print(f'Time: {time} overall {overall}')
                # print('---')

            positions: list[tuple[int, int]] = []
            q1 = 0
            q2 = 0
            q3 = 0
            q4 = 0
            # print(f'HORIZ_WALL {HORIZ_WALL} VERT_WALL {VERT_WALL}')
            for x, y, _, __ in robots:
                actual_x = x % COLS
                actual_y = y % ROWS

                if actual_x < VERT_WALL:
                    if actual_y < HORIZ_WALL:
                        # print(f'1 x {x} y {y} actual_x {actual_x} actual_y {actual_y}')
                        q1 += 1
                    elif actual_y > HORIZ_WALL:
                        # print(f'2 x {x} y {y} actual_x {actual_x} actual_y {actual_y}')
                        q3 += 1
                elif actual_x > VERT_WALL:
                    if actual_y < HORIZ_WALL:
                        # print(f'3 x {x} y {y} actual_x {actual_x} actual_y {actual_y}')
                        q2 += 1

                    elif actual_y > HORIZ_WALL:
                        # print(f'4 x {x} y {y} actual_x {actual_x} actual_y {actual_y}')
                        q4 += 1

            # print(robots)
            # print(positions)

            pt_1_res = str(q1 * q2 * q3 * q4)

        with open(join("src", "d14", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            robots: list[list[int, int, int, int]] = []

            while line:
                # a = search(r'Button A: X\+(\d*), Y\+(\d*)', line)
                vals = search(r"p=(\d*),(\d*) v=(-?\d*),(-?\d*)", line)
                robots.append(
                    [
                        int(vals.group(1)),
                        int(vals.group(2)),
                        int(vals.group(3)),
                        int(vals.group(4)),
                    ]
                )

                line = f.readline()

            # part 2: 6587

            l = len(robots)
            found_tree = False
            for time in range(PT_2_UPPER):
                for i in range(l):
                    robots[i][0] = robots[i][0] + robots[i][2]
                    robots[i][1] = robots[i][1] + robots[i][3]

                # The assumption here is the picture looks like:
                # ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
                # ●○○○○○○○○○○○○○○○○○○○○○○○○○○○○○●
                # ●○○○○○○○○○○○○○○○○○○○○○○○○○○○○○●
                # ●○○○○○○○○○○○○○○○○○○○○○○○○○○○○○●
                # ●○○○○○○○○○○○○○○○○○○○○○○○○○○○○○●
                # ●○○○○○○○○○○○○○○●○○○○○○○○○○○○○○●
                # ●○○○○○○○○○○○○○●●●○○○○○○○○○○○○○●
                # ●○○○○○○○○○○○○●●●●●○○○○○○○○○○○○●
                # ●○○○○○○○○○○○●●●●●●●○○○○○○○○○○○●
                # ●○○○○○○○○○○●●●●●●●●●○○○○○○○○○○●
                # ●○○○○○○○○○○○○●●●●●○○○○○○○○○○○○●
                # ●○○○○○○○○○○○●●●●●●●○○○○○○○○○○○●
                # ●○○○○○○○○○○●●●●●●●●●○○○○○○○○○○●
                # ●○○○○○○○○○●●●●●●●●●●●○○○○○○○○○●
                # ●○○○○○○○○●●●●●●●●●●●●●○○○○○○○○●
                # ●○○○○○○○○○○●●●●●●●●●○○○○○○○○○○●
                # ●○○○○○○○○○●●●●●●●●●●●○○○○○○○○○●
                # ●○○○○○○○○●●●●●●●●●●●●●○○○○○○○○●
                # ●○○○○○○○●●●●●●●●●●●●●●●○○○○○○○●
                # ●○○○○○○●●●●●●●●●●●●●●●●●○○○○○○●
                # ●○○○○○○○○●●●●●●●●●●●●●○○○○○○○○●
                # ●○○○○○○○●●●●●●●●●●●●●●●○○○○○○○●
                # ●○○○○○○●●●●●●●●●●●●●●●●●○○○○○○●
                # ●○○○○○●●●●●●●●●●●●●●●●●●●○○○○○●
                # ●○○○○●●●●●●●●●●●●●●●●●●●●●○○○○●
                # ●○○○○○○○○○○○○○●●●○○○○○○○○○○○○○●
                # ●○○○○○○○○○○○○○●●●○○○○○○○○○○○○○●
                # ●○○○○○○○○○○○○○●●●○○○○○○○○○○○○○●
                # ●○○○○○○○○○○○○○○○○○○○○○○○○○○○○○●
                # ●○○○○○○○○○○○○○○○○○○○○○○○○○○○○○●
                # ●○○○○○○○○○○○○○○○○○○○○○○○○○○○○○●
                # ●○○○○○○○○○○○○○○○○○○○○○○○○○○○○○●
                # ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
                # To keep things simple, this code just looks for a row of 30 ●'s
                # (the top row of the frame)

                locs: list[list[str]] = [["○"] * COLS for _ in range(ROWS)]
                for x, y, _, __ in robots:
                    col = x % COLS
                    row = y % ROWS

                    locs[row][col] = "●"

                for row in range(ROWS):
                    count = 0

                    for col in range(COLS):
                        if locs[row][col] == "●":
                            count += 1
                        else:
                            count = 0

                        if count == 30:
                            found_tree = True
                            break

                    if found_tree:
                        break

                if found_tree:
                    break

                # If the picture assumption does not work, use the following
                # code to print the picture at each time (sorry it'll be up to you to do this!)
                # print(f'time {time + 1}')
                # for row in locs:
                #     print("".join(row))
                # print('---')

            if found_tree:
                pt_2_res = str(time + 1)
            else:
                pt_2_res = "Tree is not expected shape - see code for explanation"

        return (pt_1_res, pt_2_res)
