
from re import search, findall

from typing import Literal

from os.path import join

class Day17:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.instructions = []
        self.num_instructions = 0
    
    def combo_operand(self, combo: int) -> int:
        match combo:
            case 0 | 1 | 2 | 3:
                return combo
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            
    
    def dv(self, operand: int, target: Literal['A', 'B', 'C']):
        divisor = 2 ** self.combo_operand(operand)
        res = int(self.a / divisor)
        
        match target:
            case 'A':
                self.a = res
            case 'B':
                self.b = res
            case 'C':
                self.c = res
    
    def run_program(self, a: int, b: int, c: int) -> str:
        self.a = a
        self.b = b
        self.c = c
        
        ins_ptr = 0
        output = []
        
        while ins_ptr < self.num_instructions:
            if ins_ptr == self.num_instructions - 1:
                print(f'Problem: cannot get operand because ins_ptr is at last instruction')
                return ''

            # print(f'self.a {self.a} self.b {self.b} self.c {self.c} ins_ptr {ins_ptr} output {self.output}')

            instruction = self.instructions[ins_ptr]
            operand = self.instructions[ins_ptr + 1]
            # print(f'instruction {instruction} operand {operand}')
            new_ins_ptr = ins_ptr + 2

            match instruction:
                case 0:
                    self.dv(operand, 'A')
                case 6:
                    self.dv(operand, 'B')
                case 7:
                    self.dv(operand, 'C')
                case 1:
                    self.b = self.b ^ operand
                case 2:
                    self.b = self.combo_operand(operand) % 8
                case 3:
                    # is this right??
                    # opcode 3 | jnz
                    # do nothing if register A is 0
                    #  increment instruction pointer by 2 as usual
                    # set instruction pointer to literal value
                    #  dont increment instruction pointer
                    if self.a != 0:
                        new_ins_ptr = operand
                case 4:
                    self.b = self.b ^ self.c
                case 5:
                    output.append(self.combo_operand(operand) % 8)
            
            ins_ptr = new_ins_ptr

        return ",".join(list(map(str, output)))

    def solve(self):
        with open(
            join('src', 'd17', 'input.txt'), encoding="utf-8"
        ) as f:
            line = f.readline()
            orig_a = int(search(r'\d+', line).group())

            line = f.readline()
            orig_b = int(search(r'\d+', line).group())

            line = f.readline()
            orig_c = int(search(r'\d+', line).group())

            line = f.readline()
            line = f.readline()

            self.instructions = list(map(lambda v: int(v), findall(r'\d+', line)))
            self.num_instructions = len(self.instructions)



            # print(f'self.a {self.a} self.b {self.b} self.c {self.c} self.instructions {self.instructions}')



            
            # print(f'self.a {self.a} self.b {self.b} self.c {self.c} ins_ptr {ins_ptr}')
                    

            
            # print(f'output ---')
            # print(self.output)

            pt_1_res = self.run_program(orig_a, orig_b, orig_c)




            print(f'pt_1_res: {pt_1_res}')
            print(f'pt_2_res: TODO')
        
        return (pt_1_res, 'TODO')



# Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0

# Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0



# Combo operands 0 through 3 represent literal values 0 through 3.
# Combo operand 4 represents the value of register A.
# Combo operand 5 represents the value of register B.
# Combo operand 6 represents the value of register C.

# opcode 0 | adv
# division
# numerator = register A
# divisor = 2 ^ (combo operand)
# result: truncated to an integer and then written to the A register

# opcode 1 | bxl
# bitwise XOR
# (register B) ^ (literal operand)
# result: stores the result in register B

# opcode 2 | bst
# combo operand % 8
# result: stores the result in register B

# opcode 3 | jnz
# do nothing if register A is 0
#  increment instruction pointer by 2 as usual
# set instruction pointer to literal value
#  dont increment instruction pointer

# opcode 4 | bxc
# bitwise XOR
# (register B) ^ (register C)
# result: stores result in register B
# (ignore operand)

# opcode 5 | out
# combo operand % 8
# output: print

# opcode 6 | bdv
# do the same as opcode 0
# except write to B register

# opcode 7 | cdv
# do the same as opcode 0
# except write to C register


