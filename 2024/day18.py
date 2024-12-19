import helpers
import copy
from collections import defaultdict
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

MAX_MAP_COORDINATE = 70
CORRUPTED_BYTES = 1024


MAP_SIZE = MAX_MAP_COORDINATE + 1
START_COORDINATE  = (0,0)
END_COORDINATE = (MAX_MAP_COORDINATE,MAX_MAP_COORDINATE)

queue = [START_COORDINATE]
weights = {START_COORDINATE: 0}

raw_locs = [i.split(',') for i in input.split("\n")][:CORRUPTED_BYTES]
bad_locs = [(int(i[0]),int(i[1])) for i in raw_locs]
# print('bad_locs',bad_locs)

def handle_position(co, weight):
  if co[0] < 0 or co[1] < 0 or co[0] > MAX_MAP_COORDINATE or co[1] > MAX_MAP_COORDINATE:
    return
  if co in bad_locs:
    return
  if co not in weights:
    weights[co] = weight
    queue.append(co)
  elif weight < weights[co]:
    weights[co] = weight
    queue.append(co)

# coordinates are (X,Y) ,distance from top left
while len(queue) > 0:
  current_co = queue.pop()
  current_co_weight = weights[current_co]
  top_co = (current_co[0],current_co[1]-1)
  bottom_co = (current_co[0],current_co[1]+1)
  left_co = (current_co[0]-1,current_co[1])
  right_co = (current_co[0]+1,current_co[1])
  handle_position(top_co, current_co_weight+1)
  handle_position(bottom_co, current_co_weight+1)
  handle_position(left_co, current_co_weight+1)
  handle_position(right_co, current_co_weight+1)

def print_map():
  for i in range(MAP_SIZE):
    row = ''
    for j in range(MAP_SIZE):
      if (i,j) in weights:
        row += 'O'
      elif (i,j) in bad_locs:
        row += '#'
      else:
        row += '.'
    print(row)

# print('weights',weights)
# print_map()
print('end weight:',weights[END_COORDINATE])