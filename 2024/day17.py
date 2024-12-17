import helpers
import copy
from collections import defaultdict
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input


input_lines = input.split("\n")

a = int(input_lines[0].split(": ")[1])
b = 0
c = 0

registers = {
  'a': a,
  'b': b,
  'c': c,
}

def parse_program(input_lines):
  program = input_lines[4].split(": ")[1]
  indvidual_instructions = program.split(',')
  indvidual_instructions = [int(i) for i in indvidual_instructions]
  instructions = []
  current_instruction = []
  for i,indvidual_instruction in enumerate(indvidual_instructions):
    if i%2 == 0:
      current_instruction.append(indvidual_instruction)
    else:
      current_instruction.append(indvidual_instruction)
      instructions.append(current_instruction)
      current_instruction = []
  return instructions

print(parse_program(input_lines))

def get_combo(operand):
  a = registers['a']
  b = registers['b']
  c = registers['c']
  if operand <= 3:
    return operand
  if operand == 4:
    return a
  if operand == 5:
    return b
  if operand == 6:
    return c
  print('combo operand 7', operand)
  return None

all_outs = []
def run_instruction(instruction, instruction_pointer, registers):
  print('running',instruction,'pointer',instruction_pointer, 'registers',registers)
  a = registers['a']
  b = registers['b']
  c = registers['c']
  opcode = instruction[0]
  operand = instruction[1]
  combo = get_combo(operand)
  # The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.
  if opcode == 0:
    registers['a'] = a//(2**combo)
    instruction_pointer += 2//2
  # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
  if opcode == 1:
    registers['b'] = b ^ operand
    instruction_pointer += 2//2
  # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
  if opcode == 2:
    registers['b'] = combo % 8
    instruction_pointer += 2//2
  # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
  if opcode == 3:
    if a != 0:
      instruction_pointer = operand//2
    else:
      instruction_pointer += 2//2
  # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
  if opcode == 4:
    registers['b'] = b ^ c
    instruction_pointer += 2//2
  # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
  if opcode == 5:
    out = combo % 8
    print('out', out)
    all_outs.append(out)
    instruction_pointer += 2//2
  # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
  if opcode == 6:
    registers['b'] = a//(2**combo)
    instruction_pointer += 2//2
  # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
  if opcode == 7:
    registers['c'] = a//(2**combo)
    instruction_pointer += 2//2
  return instruction_pointer,registers

instructions = parse_program(input_lines)
instruction_pointer = 0
# for i in range(4):
while instruction_pointer < len(instructions):
  instruction = instructions[instruction_pointer]
  instruction_pointer,registers = run_instruction(instruction, instruction_pointer, registers)

print(','.join([str(i) for i in all_outs]))
