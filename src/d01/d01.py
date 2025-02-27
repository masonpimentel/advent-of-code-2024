from collections import Counter

from os.path import join

class Day01:
    def solve(self):
        with open(
            join('src', 'd01', 'input.txt'), encoding="utf-8"
        ) as f:
            left: list[int] = []
            right: list[int] = []

            line = f.readline()
            while line:
                left_val, right_val = line.split('   ')

                left.append(int(left_val))
                right.append(int(right_val))

                line = f.readline()
            
            left.sort()
            right.sort()

            difference = 0
            for i in range(len(left)):
                difference += abs(left[i] - right[i])
            
            print(f'pt_1_res: {difference}')

            right_counts = Counter(right)

            similarity = 0
            for val in left:
                if val in right_counts:
                    similarity += (val * right_counts[val])
            
            print(f'pt_2_res: {similarity}')
            
        return (str(difference), str(similarity))