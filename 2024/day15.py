import helpers
import copy
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

def convert_to_bigger_map(map):
  new_map = []
  for row in map:
    new_row = []
    for char in row:
      if char == '#':
        new_row.append('#')
        new_row.append('#')
      elif char == "O":
        new_row.append('[')
        new_row.append(']')
      elif char == ".":
        new_row.append('.')
        new_row.append('.')
      elif char == "@":
        new_row.append('@')
        new_row.append('.')
    new_map.append(new_row)
  return new_map


def parse_input(input_str):
  i = input_str.split("\n\n")
  map = helpers.parse_map_from_input(i[0])
  map = [list(row) for row in map]
  map = convert_to_bigger_map(map)
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

def can_move_up(map,loc):
  next_loc_char = map[loc[0]-1][loc[1]]
  if next_loc_char == '.':
    return True
  if next_loc_char == '#':
    return False
  if next_loc_char == '[':
    up_left = (loc[0]-1, loc[1])
    up_right = (loc[0]-1, loc[1]+1)
    return (can_move_up(map,up_left) and can_move_up(map,up_right))
  if next_loc_char == ']':
    up_left = (loc[0]-1, loc[1]-1)
    up_right = (loc[0]-1, loc[1])
    return (can_move_up(map,up_left) and can_move_up(map,up_right))
  
def move_up(map,loc):
  current_char =  map[loc[0]][loc[1]]
  next_loc_char = map[loc[0]-1][loc[1]]
  if next_loc_char == '.':
    map[loc[0]-1][loc[1]] = current_char
    map[loc[0]][loc[1]] = '.'
    return (loc[0]-1, loc[1])
  if next_loc_char == '#':
    return (loc[0], loc[1])
  if next_loc_char == '[':
    up_left = (loc[0]-1, loc[1])
    up_right = (loc[0]-1, loc[1]+1)
    move_up(map,up_left)
    move_up(map,up_right)
    map[loc[0]-1][loc[1]] = current_char
    map[loc[0]][loc[1]] = '.'
    return (loc[0]-1, loc[1])
  if next_loc_char == ']':
    up_left = (loc[0]-1, loc[1]-1)
    up_right = (loc[0]-1, loc[1])
    move_up(map,up_left)
    move_up(map,up_right)
    map[loc[0]-1][loc[1]] = current_char
    map[loc[0]][loc[1]] = '.'
    return (loc[0]-1, loc[1])

def can_move_down(map,loc):
  next_loc_char = map[loc[0]+1][loc[1]]
  if next_loc_char == '.':
    return True
  if next_loc_char == '#':
    return False
  if next_loc_char == '[':
    down_left = (loc[0]+1, loc[1])
    down_right = (loc[0]+1, loc[1]+1)
    return (can_move_down(map,down_left) and can_move_down(map,down_right))
  if next_loc_char == ']':
    down_left = (loc[0]+1, loc[1]-1)
    down_right = (loc[0]+1, loc[1])
    return (can_move_down(map,down_left) and can_move_down(map,down_right))
  
def move_down(map,loc):
  current_char =  map[loc[0]][loc[1]]
  next_loc_char = map[loc[0]+1][loc[1]]
  if next_loc_char == '.':
    map[loc[0]+1][loc[1]] = current_char
    map[loc[0]][loc[1]] = '.'
    return (loc[0]+1, loc[1])
  if next_loc_char == '#':
    return (loc[0], loc[1])
  if next_loc_char == '[':
    down_left = (loc[0]+1, loc[1])
    down_right = (loc[0]+1, loc[1]+1)
    move_down(map,down_left)
    move_down(map,down_right)
    map[loc[0]+1][loc[1]] = current_char
    map[loc[0]][loc[1]] = '.'
    return (loc[0]+1, loc[1])
  if next_loc_char == ']':
    down_left = (loc[0]+1, loc[1]-1)
    down_right = (loc[0]+1, loc[1])
    move_down(map,down_left)
    move_down(map,down_right)
    map[loc[0]+1][loc[1]] = current_char
    map[loc[0]][loc[1]] = '.'
    return (loc[0]+1, loc[1])

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
  # print('taking step from ',loc)
  if move == '<':
    return move_left(map,loc)
  elif move == '^' and can_move_up(map,loc):
    return move_up(map,loc)
  elif move == 'v' and can_move_down(map,loc):
    return move_down(map,loc)
  elif move == '>':
    return move_right(map,loc)
  else:
    return(loc)

def print_map_with_loc(map,loc):
  map_copy = copy.deepcopy(map)
  map_copy[loc[0]][loc[1]] = "@"
  print("\n".join([''.join(row) for row in map_copy]))


map,moves = parse_input(input)

# print(moves)
loc = find_start(map)
print_map_with_loc(map,loc)
# # start = (1,4)
# map[start[0]][start[1]] = '.'

def calculate_gps(map):
  total = 0
  height = len(map)
  for i,row in enumerate(map):
    for j,char in enumerate(row):
      if char == '[':
        x = min(i,height-i-1)
        # y = min(j,width-j)
        # box_score = (x*100) + j
        box_score = (i*100) + j
        print('box at',i,j,'x is',x,'score is',box_score)
        total += box_score
  return total

# print( calculate_gps(map))
for i,move in enumerate(moves):
  # print('at', loc, 'moving ',move, ', current map:')
  # print_map_with_loc(map,loc)
  # print(i,'moving',move, ', current map:')
  loc = take_step(map,loc,move)
  # print('finished moving ',move,' now at ',loc)
  # print('===================')
print(loc)
print_map_with_loc(map,loc)
print( calculate_gps(map))