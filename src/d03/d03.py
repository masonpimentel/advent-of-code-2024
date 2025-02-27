from re import findall

from os.path import join

class Day03:
    def solve(self):
        with open(
            join('src', 'd03', 'input.txt'), encoding="utf-8"
        ) as f:
            line = f.readline()

            
            
            full_input = ''
            disabling_input = ''
            is_add = True
            s: list[str] = []
            
            while line:
                for i, c in enumerate(line):
                    full_input += c

                    if line[i : i + 7] == "don't()":
                        is_add = False

                    if "".join(s[-4:]) == "do()":
                        is_add = True
                        s = s[:-4]

                    if is_add:
                        disabling_input += c
                    
                    s.append(c)


                line = f.readline()

            no_disabling = 0
            disabling = 0

            no_disabling_matches = findall(r'mul\((\d*),(\d*)\)', full_input)
            for v1, v2 in no_disabling_matches:
                no_disabling += (int(v1) * int(v2))

            disabling_matches = findall(r'mul\((\d*),(\d*)\)', disabling_input)
            for v1, v2 in disabling_matches:
                disabling += (int(v1) * int(v2))
            
            print(f'pt_1_res: {no_disabling}')
            print(f'pt_2_res: {disabling}')
        
        return (str(no_disabling), str(disabling))