from os.path import join

class Day19:
    def solve(self):
        with open(
            join('src', 'd19', 'input.txt'), encoding="utf-8"
        ) as f:
            line = f.readline()


            possible = set(line[:-1].split(', '))

            line = f.readline()

            dp: dict[str, int] = {}

            def rec(pat: str) -> int:
                if pat == '':
                    return 1
                
                res = 0
                for i in range(len(pat)):
                    complete = pat[:i + 1]

                    if complete in possible:
                        
                        new_pat = pat[i + 1:]

                        if new_pat in dp:
                            attempt = dp[new_pat]
                        else:
                            attempt = rec(new_pat)
                            dp[new_pat] = attempt

                        res += attempt
                
                

                return res

            line = f.readline()
            pt_1_res = 0
            pt_2_res = 0
            i = 1
            while line:
                pat = line[:-1] if line[-1] == '\n' else line

                attempt = rec(pat)

                
                pt_1_res += 1 if attempt > 0 else 0
                pt_2_res += attempt

                line = f.readline()

                # i += 1
            
            print(f'pt_1_res: {pt_1_res}')
            print(f'pt_2_res: {pt_2_res}')
        
        return (str(pt_1_res), str(pt_2_res))
