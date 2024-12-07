import helpers
from itertools import permutations 
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

eqs = input.split("\n")

def is_solvable(value, inputs):
  if int(value) != value:
      return False
  value = int(value)
  if len(inputs) == 1:
    if inputs[0] == value:
      print('value',value, 'inputs', inputs)
      return True
    else:
      return False
  print('value', value, "inputs", inputs)
  # last_two = int(str(inputs[-2]) + str(inputs[-1]))
  # concat_inputs = inputs[:-2] + [last_two]
  # print('inputs:', inputs, 'last_two', last_two, 'contact: ',concat_inputs)
  chars_to_remove = len(str(inputs[-1]))
  if len(str(value)) > chars_to_remove and str(value)[-chars_to_remove:] == str(inputs[-1]):
    # print('value', value, "inputs", inputs)
    value_without_last_char = int(str(int(value))[:-chars_to_remove])
    return is_solvable(value-inputs[-1], inputs[:-1]) or is_solvable(value/inputs[-1], inputs[:-1]) or is_solvable(value_without_last_char, inputs[:-1])
  else: 
    # print('value', value,'len(str(value))', len(str(value)), 'inputs', inputs, 'chars_to_remove', chars_to_remove)
    return is_solvable(value-inputs[-1], inputs[:-1]) or is_solvable(value/inputs[-1], inputs[:-1]) 


total = 0
# max_length = 0
for eq in eqs:
  # total += solve(eq)
  print('---------')
  value = int(eq.split(': ')[0])
  print(value)
  print('---------')

  inputs = [int(i) for i in eq.split(': ')[1].split(' ')]
  if is_solvable(value, inputs):
    print('solvable', value)
    total += value
  else:
    print('NOT solvableable', value)
print(total)

# 3782298305575 is not right
# 3782298305575 is not right