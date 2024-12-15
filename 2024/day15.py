import helpers
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input
import copy

def parse_input(input_str):
  i = input_str.split("\n\n")
  map = helpers.parse_map_from_input(i[0])
  map = [list(row) for row in map]
  moves = i[1]
  moves = moves.replace("\n", "")
  return (map,moves)

def find_start(map):
  for i,row in enumerate(map):
    for j,char in enumerate(row):
      if char == '@':
        row[j] = '.'
        return (i,j)
      
def move_left(map,loc):
  spaces_to_move_left = 0
  next_loc_char = map[loc[0]][loc[1]-(spaces_to_move_left+1)]
  while next_loc_char != '#':
    spaces_to_move_left += 1
    if next_loc_char == '.':
      break
    next_loc_char = map[loc[0]][loc[1]-(spaces_to_move_left+1)]
  # print('spaces_to_move_left',spaces_to_move_left)
  if next_loc_char == '#':
    return (loc[0],loc[1])
  for i in reversed(range(spaces_to_move_left)):
    target_loc = (loc[0],loc[1]-i-1)
    moving_char = map[loc[0]][loc[1]-i]
    # print('i',i,'target_loc',target_loc,'moving_char',moving_char)
    map[loc[0]][loc[1]-i-1] = moving_char
  return (loc[0],loc[1]-(min(spaces_to_move_left,1)))

def move_up(map,loc):
  spaces_to_move = 0
  next_loc_char = map[loc[0]-(spaces_to_move+1)][loc[1]]
  print('moving up, next_loc_char', next_loc_char)
  while next_loc_char != '#':
    spaces_to_move += 1
    if next_loc_char == '.':
      break
    next_loc_char = map[loc[0]-(spaces_to_move+1)][loc[1]]
  if next_loc_char == '#':
    return (loc[0],loc[1])
  for i in reversed(range(spaces_to_move)):
    target_loc = (loc[0]-i-1,loc[1])
    moving_char = map[loc[0]-i][loc[1]]
    map[loc[0]-i-1][loc[1]] = moving_char
  return (loc[0]-(min(spaces_to_move,1)),loc[1])

def move_down(map,loc):
  spaces_to_move = 0
  next_loc_char = map[loc[0]+(spaces_to_move+1)][loc[1]]
  while next_loc_char != '#':
    spaces_to_move += 1
    if next_loc_char == '.':
      break
    next_loc_char = map[loc[0]+(spaces_to_move+1)][loc[1]]
  if next_loc_char == '#':
    return (loc[0],loc[1])
  for i in reversed(range(spaces_to_move)):
    target_loc = (loc[0]+i+1,loc[1])
    moving_char = map[loc[0]+i][loc[1]]
    map[loc[0]+i+1][loc[1]] = moving_char
  return (loc[0]+(min(spaces_to_move,1)),loc[1])


def move_right(map,loc):
  print("above to move right from loc",loc)
  spaces_to_move = 0
  next_loc_char = map[loc[0]][loc[1]+(spaces_to_move+1)]
  while next_loc_char != '#':
    spaces_to_move += 1
    if next_loc_char == '.':
      break
    next_loc_char = map[loc[0]][loc[1]+(spaces_to_move+1)]
  if next_loc_char == '#':
    return (loc[0],loc[1])
  for i in reversed(range(spaces_to_move)):
    target_loc = (loc[0],loc[1]+i+1)
    moving_char = map[loc[0]][loc[1]+i]
    map[loc[0]][loc[1]+i+1] = moving_char
  end_loc = (loc[0],loc[1]+(min(spaces_to_move,1)))
  print('moved to',end_loc)
  return end_loc
      
def take_step(map,loc,move):
  print('taking step from ',loc)
  if move == '<':
    return move_left(map,loc)
  elif move == '^':
    return move_up(map,loc)
  elif move == 'v':
    return move_down(map,loc)
  elif move == '>':
    return move_right(map,loc)

def print_map_with_loc(map,loc):
  map_copy = copy.deepcopy(map)
  map_copy[loc[0]][loc[1]] = "@"
  print("\n".join([''.join(row) for row in map_copy]))


map,moves = parse_input(input)
print(map)
print(moves)
start = find_start(map)
# start = (1,4)
map[start[0]][start[1]] = '.'

def calculate_gps(map):
  total = 0
  for i,row in enumerate(map):
    for j,char in enumerate(row):
      if char == 'O':
        total += (100*i) + j
  return total

loc=start
for move in moves:
  print('at', loc, 'moving ',move, ', current map:')
  # print_map_with_loc(map,loc)
  # print('at', loc, 'moving ',move, ', current map:')
  loc = take_step(map,loc,move)
  # print('finished moving ',move,' now at ',loc)
  print('===================')
print(loc)
print_map_with_loc(map,loc)
print( calculate_gps(map))