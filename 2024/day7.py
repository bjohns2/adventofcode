import helpers
from itertools import permutations 
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

eqs = input.split("\n")

def is_solvable(value, inputs):
  if int(value) != value:
      return False
  if len(inputs) == 1:
    if inputs[0] == value:
     return True
    else:
      return False
  return is_solvable(value-inputs[-1], inputs[:-1]) or is_solvable(value/inputs[-1], inputs[:-1])

total = 0
# max_length = 0
for eq in eqs:
  # total += solve(eq)
  value = int(eq.split(': ')[0])
  inputs = [int(i) for i in eq.split(': ')[1].split(' ')]
  if is_solvable(value, inputs):
    total += value
print(total)

