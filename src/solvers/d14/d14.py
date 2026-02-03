"""Day 13"""

from re import search
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


class Day14(Day):
    """Restroom Redoubt"""

    COLS = 101
    ROWS = 103

    HORIZ_WALL = ROWS // 2
    VERT_WALL = COLS // 2

    PT_2_UPPER = 100000
    PT_2_TREE_BORDER = 20

    def __init__(self) -> None:
        self.pt_1_robots: list[list[int]] = []
        self.pt_2_robots: list[list[int]] = []
        self.num_robots = 0

    def get_pt_1(self) -> str:
        for _ in range(100):
            for i in range(self.num_robots):
                self.pt_1_robots[i][0] = self.pt_1_robots[i][0] + self.pt_1_robots[i][2]
                self.pt_1_robots[i][1] = self.pt_1_robots[i][1] + self.pt_1_robots[i][3]

        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        for x, y, _, __ in self.pt_1_robots:
            actual_x = x % self.COLS
            actual_y = y % self.ROWS

            if actual_x < self.VERT_WALL:
                if actual_y < self.HORIZ_WALL:
                    q1 += 1
                elif actual_y > self.HORIZ_WALL:
                    q3 += 1
            elif actual_x > self.VERT_WALL:
                if actual_y < self.HORIZ_WALL:
                    q2 += 1

                elif actual_y > self.HORIZ_WALL:
                    q4 += 1

        return str(q1 * q2 * q3 * q4)

    def get_pt_2(self) -> str:
        found_tree = False
        for time in range(self.PT_2_UPPER):
            for i in range(self.num_robots):
                self.pt_2_robots[i][0] = self.pt_2_robots[i][0] + self.pt_2_robots[i][2]
                self.pt_2_robots[i][1] = self.pt_2_robots[i][1] + self.pt_2_robots[i][3]

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
            # To keep things simple, this code just looks for a row of 20 ●'s
            # (the top row of the frame)
            # Unfortunately this will fail if a row of 20 coincidentally
            # appears on another arrangement

            locs: list[list[str]] = [["○"] * self.COLS for _ in range(self.ROWS)]
            for x, y, _, __ in self.pt_2_robots:
                col = x % self.COLS
                row = y % self.ROWS

                locs[row][col] = "●"

            for row in range(self.ROWS):
                count = 0

                for col in range(self.COLS):
                    if locs[row][col] == "●":
                        count += 1
                    else:
                        count = 0

                    if count == self.PT_2_TREE_BORDER:
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
            return str(time + 1)

        return "Tree is not expected shape - see code for explanation"

    def solve(self) -> SolveInfo:
        with open(get_path("14"), encoding="utf-8") as f:
            robots: list[list[int]] = []

            line = f.readline()
            while line:
                vals = search(r"p=(\d*),(\d*) v=(-?\d*),(-?\d*)", line)
                if vals:
                    robots.append(
                        [
                            int(vals.group(1)),
                            int(vals.group(2)),
                            int(vals.group(3)),
                            int(vals.group(4)),
                        ]
                    )

                line = f.readline()

            self.pt_1_robots = [list(robot) for robot in robots]
            self.pt_2_robots = [list(robot) for robot in robots]
            self.num_robots = len(robots)

        return SolveInfo(self.get_pt_1(), self.get_pt_2())
