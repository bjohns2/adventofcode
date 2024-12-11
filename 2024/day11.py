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

cache = {}

def recursive_blink(rock, i):
  rock_str = f"{rock},{i}"
  if rock_str in cache:
    return cache[rock_str]
  if i == 0:
    return 1
  if rock == 0:
    length = recursive_blink(1, i-1)
  elif len(str(rock)) % 2 == 0:
    slice_index = int(len(str(rock))/2)
    first_half = int(str(rock)[:slice_index])
    second_half = int(str(rock)[slice_index:])
    length = recursive_blink(first_half, i-1) + recursive_blink(second_half, i-1)
  else:
    length = recursive_blink(rock*2024, i-1)
  cache[rock_str] = length
  return length

total = 0
for rock in start_rocks:
  total += recursive_blink(rock, 75)
  print(rock, total)
print(total)
