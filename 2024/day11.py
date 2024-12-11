import helpers
import math
import copy
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

start_rocks = [int(i) for i in input.split(' ')]

def blink(rocks):
  new_rocks = copy.deepcopy(rocks)
  updates_to_make = []
  for i, rock in enumerate(rocks):
    if rock == 0:
      new_rocks[i] = 1
    elif len(str(rock)) % 2 == 0:
      slice_index = int(len(str(rock))/2)
      first_half = int(str(rock)[:slice_index])
      second_half = int(str(rock)[slice_index:])
      # print(rock, 'becomes', first_half, second_half)
      updates_to_make.append([i,first_half,second_half])
    else:
      new_rocks[i] = rocks[i] * 2024
  while len(updates_to_make) > 0:
    update = updates_to_make.pop()
    new_rocks[update[0]] = update[2]
    new_rocks.insert(update[0], update[1])
  return new_rocks

for i in range(0,25):
  start_rocks = blink(start_rocks)

print(len(start_rocks))
 