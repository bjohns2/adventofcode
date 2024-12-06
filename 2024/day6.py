import helpers
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

map = helpers.parse_map_from_input(input)

POS_CHARS = ['^', 'v', '<', '>']
OBSTRUCTION = '#'

def find_start_position(map):
  for i, row in enumerate(map):
    for j, pos in enumerate(row):
      if pos == '^':
        return  [i,j, 'up']
      if pos == 'v':
        return  [i,j, 'down']
      if pos == '<':
        return  [i,j, 'left']
      if pos == '>':
        return  [i,j, 'right']
      
def step(map, pos):
      i = pos[0]
      j = pos[1]
      direction = pos[2]
      if direction == 'up':
        if position_is_valid(map, i-1,j) and map[i-1][j] == OBSTRUCTION:
          return [i, j+1, 'right']
        else:
          return [i-1,j, 'up']
      if direction == 'down':
        if position_is_valid(map, i+1,j) and map[i+1][j] == OBSTRUCTION:
          return [i, j-1, 'left']
        else:
          return [i+1,j, 'down']
      if direction == 'right':
        if position_is_valid(map, i,j+1) and map[i][j+1] == OBSTRUCTION:
          return [i+1, j, 'down']
        else:
          return [i,j+1, 'right']
      if direction == 'left':
        if position_is_valid(map, i,j-1) and map[i][j-1] == OBSTRUCTION:
          return [i-1, j, 'up']
        else:
          return [i,j-1, 'left']
        
def position_is_valid(map, i,j):
  return i >= 0 and j >= 0 and i < len(map) and j < len(map[0])
      
position = find_start_position(map)
all_positions = set()

new_map = helpers.parse_map_from_input(input)


while position_is_valid(map, position[0], position[1]):
  position = step(map, position)
  i = position[0]
  j = position[1]
  if position_is_valid(map, i,j):
    new_position_str = f"{position[0]},{position[1]}"
    updated_row = new_map[position[0]]
    new_map[i] = updated_row[:j] + 'X' + updated_row[j + 1:]
    all_positions.add(new_position_str)

new_map_str = ""
for row in new_map:
  new_map_str = new_map_str + "\n" +  row
print(new_map_str)


print(len(all_positions))