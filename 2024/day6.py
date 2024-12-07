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
          return [i, j, 'right']
        else:
          return [i-1,j, 'up']
      if direction == 'down':
        if position_is_valid(map, i+1,j) and map[i+1][j] == OBSTRUCTION:
          return [i, j, 'left']
        else:
          return [i+1,j, 'down']
      if direction == 'right':
        if position_is_valid(map, i,j+1) and map[i][j+1] == OBSTRUCTION:
          return [i, j, 'down']
        else:
          return [i,j+1, 'right']
      if direction == 'left':
        if position_is_valid(map, i,j-1) and map[i][j-1] == OBSTRUCTION:
          return [i, j, 'up']
        else:
          return [i,j-1, 'left']
        
def position_is_valid(map, i,j):
  return (i >= 0 and j >= 0 and i < len(map) and j < len(map[0]))
      
start_position = find_start_position(map)

new_map = helpers.parse_map_from_input(input)

def iterate_obstructions(map):
  loops = 0
  total = len(map)
  for i, row in enumerate(map):
    print(f"Checking row {i} of {total} for obstructions. {loops} loops so far!")
    for j, pos in enumerate(row):
      # print(f"Checking {i},{j} for obstructions. {loops} loops so far!")
      # skip the location if it's already an obstrution or the start position
      if pos in ['#', '^', 'v', '<', '>']:
        continue
      new_map = helpers.parse_map_from_input(input)
      updated_row = new_map[i]
      new_map[i] = updated_row[:j] + '#' + updated_row[j + 1:]
      # print(f"==={i},{j}====")
      # helpers.print_map(new_map)
      # print('=======')
      if found_loop(new_map, start_position):
        loops += 1
  print("total loops:",loops)

def found_loop(map, start_position):
  start_position_str = f"{start_position[0]},{start_position[1]},{start_position[2]}"
  all_positions = [start_position_str]
  position = start_position
  while position_is_valid(map, position[0], position[1]):
    position = step(map, position)
    i = position[0]
    j = position[1]
    d = position[2]
    new_position_str = f"{i},{j},{d}"
    if new_position_str in all_positions:
      return True
    all_positions.append(new_position_str)
  return False

# helpers.print_map(new_map)
iterate_obstructions(map)

# print(len(all_positions))

# 1706 is too low
# 1707 also too low

# Checking row 0 of 130 for obstructions. 0 loops so far!
# Checking row 1 of 130 for obstructions. 0 loops so far!
# Checking row 2 of 130 for obstructions. 0 loops so far!
# Checking row 3 of 130 for obstructions. 0 loops so far!
# Checking row 4 of 130 for obstructions. 0 loops so far!
# Checking row 5 of 130 for obstructions. 0 loops so far!
# Checking row 6 of 130 for obstructions. 27 loops so far!
# Checking row 7 of 130 for obstructions. 28 loops so far!
# Checking row 8 of 130 for obstructions. 71 loops so far!
# Checking row 9 of 130 for obstructions. 74 loops so far!
# Checking row 10 of 130 for obstructions. 92 loops so far!
# Checking row 11 of 130 for obstructions. 95 loops so far!
# Checking row 12 of 130 for obstructions. 140 loops so far!
# Checking row 13 of 130 for obstructions. 143 loops so far!
# Checking row 14 of 130 for obstructions. 147 loops so far!
# Checking row 15 of 130 for obstructions. 150 loops so far!
# Checking row 16 of 130 for obstructions. 159 loops so far!
# Checking row 17 of 130 for obstructions. 178 loops so far!
# Checking row 18 of 130 for obstructions. 184 loops so far!
# Checking row 19 of 130 for obstructions. 205 loops so far!
# Checking row 20 of 130 for obstructions. 212 loops so far!
# Checking row 21 of 130 for obstructions. 238 loops so far!
# Checking row 22 of 130 for obstructions. 279 loops so far!
# Checking row 23 of 130 for obstructions. 289 loops so far!
# Checking row 24 of 130 for obstructions. 305 loops so far!
# Checking row 25 of 130 for obstructions. 316 loops so far!
# Checking row 26 of 130 for obstructions. 324 loops so far!
# Checking row 27 of 130 for obstructions. 356 loops so far!
# Checking row 28 of 130 for obstructions. 366 loops so far!
# Checking row 29 of 130 for obstructions. 400 loops so far!
# Checking row 30 of 130 for obstructions. 414 loops so far!
# Checking row 31 of 130 for obstructions. 434 loops so far!
# Checking row 32 of 130 for obstructions. 442 loops so far!
# Checking row 33 of 130 for obstructions. 452 loops so far!
# Checking row 34 of 130 for obstructions. 491 loops so far!
# Checking row 35 of 130 for obstructions. 513 loops so far!
# Checking row 36 of 130 for obstructions. 524 loops so far!
# Checking row 37 of 130 for obstructions. 543 loops so far!
# Checking row 38 of 130 for obstructions. 559 loops so far!
# Checking row 39 of 130 for obstructions. 570 loops so far!
# Checking row 40 of 130 for obstructions. 596 loops so far!
# Checking row 41 of 130 for obstructions. 613 loops so far!
# Checking row 42 of 130 for obstructions. 624 loops so far!
# Checking row 43 of 130 for obstructions. 626 loops so far!
# Checking row 44 of 130 for obstructions. 636 loops so far!
# Checking row 45 of 130 for obstructions. 673 loops so far!
# Checking row 46 of 130 for obstructions. 710 loops so far!
# Checking row 47 of 130 for obstructions. 742 loops so far!
# Checking row 48 of 130 for obstructions. 755 loops so far!
# Checking row 49 of 130 for obstructions. 761 loops so far!
# Checking row 50 of 130 for obstructions. 767 loops so far!
# Checking row 51 of 130 for obstructions. 772 loops so far!
# Checking row 52 of 130 for obstructions. 804 loops so far!
# Checking row 53 of 130 for obstructions. 810 loops so far!
# Checking row 54 of 130 for obstructions. 832 loops so far!
# Checking row 55 of 130 for obstructions. 855 loops so far!
# Checking row 56 of 130 for obstructions. 864 loops so far!
# Checking row 57 of 130 for obstructions. 908 loops so far!
# Checking row 58 of 130 for obstructions. 921 loops so far!
# Checking row 59 of 130 for obstructions. 938 loops so far!
# Checking row 60 of 130 for obstructions. 955 loops so far!
# Checking row 61 of 130 for obstructions. 976 loops so far!
# Checking row 62 of 130 for obstructions. 990 loops so far!
# Checking row 63 of 130 for obstructions. 1003 loops so far!
# Checking row 64 of 130 for obstructions. 1037 loops so far!
# Checking row 65 of 130 for obstructions. 1040 loops so far!
# Checking row 66 of 130 for obstructions. 1053 loops so far!
# Checking row 67 of 130 for obstructions. 1070 loops so far!
# Checking row 68 of 130 for obstructions. 1084 loops so far!
# Checking row 69 of 130 for obstructions. 1100 loops so far!
# Checking row 70 of 130 for obstructions. 1112 loops so far!
# Checking row 71 of 130 for obstructions. 1122 loops so far!
# Checking row 72 of 130 for obstructions. 1131 loops so far!
# Checking row 73 of 130 for obstructions. 1141 loops so far!
# Checking row 74 of 130 for obstructions. 1170 loops so far!
# Checking row 75 of 130 for obstructions. 1197 loops so far!
# Checking row 76 of 130 for obstructions. 1217 loops so far!
# Checking row 77 of 130 for obstructions. 1231 loops so far!
# Checking row 78 of 130 for obstructions. 1239 loops so far!
# Checking row 79 of 130 for obstructions. 1262 loops so far!
# Checking row 80 of 130 for obstructions. 1300 loops so far!
# Checking row 81 of 130 for obstructions. 1310 loops so far!
# Checking row 82 of 130 for obstructions. 1327 loops so far!
# Checking row 83 of 130 for obstructions. 1351 loops so far!
# Checking row 84 of 130 for obstructions. 1363 loops so far!
# Checking row 85 of 130 for obstructions. 1371 loops so far!
# Checking row 86 of 130 for obstructions. 1374 loops so far!
# Checking row 87 of 130 for obstructions. 1393 loops so far!
# Checking row 88 of 130 for obstructions. 1408 loops so far!
# Checking row 89 of 130 for obstructions. 1418 loops so far!
# Checking row 90 of 130 for obstructions. 1423 loops so far!
# Checking row 91 of 130 for obstructions. 1432 loops so far!
# Checking row 92 of 130 for obstructions. 1444 loops so far!
# Checking row 93 of 130 for obstructions. 1444 loops so far!
# Checking row 94 of 130 for obstructions. 1453 loops so far!
# Checking row 95 of 130 for obstructions. 1465 loops so far!
# Checking row 96 of 130 for obstructions. 1467 loops so far!
# Checking row 97 of 130 for obstructions. 1476 loops so far!
# Checking row 98 of 130 for obstructions. 1488 loops so far!
# Checking row 99 of 130 for obstructions. 1517 loops so far!
# Checking row 100 of 130 for obstructions. 1520 loops so far!
# Checking row 101 of 130 for obstructions. 1527 loops so far!
# Checking row 102 of 130 for obstructions. 1540 loops so far!
# Checking row 103 of 130 for obstructions. 1552 loops so far!
# Checking row 104 of 130 for obstructions. 1558 loops so far!
# Checking row 105 of 130 for obstructions. 1562 loops so far!
# Checking row 106 of 130 for obstructions. 1569 loops so far!
# Checking row 107 of 130 for obstructions. 1574 loops so far!
# Checking row 108 of 130 for obstructions. 1580 loops so far!
# Checking row 109 of 130 for obstructions. 1584 loops so far!
# Checking row 110 of 130 for obstructions. 1588 loops so far!
# Checking row 111 of 130 for obstructions. 1604 loops so far!
# Checking row 112 of 130 for obstructions. 1609 loops so far!
# Checking row 113 of 130 for obstructions. 1610 loops so far!
# Checking row 114 of 130 for obstructions. 1625 loops so far!
# Checking row 115 of 130 for obstructions. 1629 loops so far!
# Checking row 116 of 130 for obstructions. 1657 loops so far!
# Checking row 117 of 130 for obstructions. 1658 loops so far!
# Checking row 118 of 130 for obstructions. 1661 loops so far!
# Checking row 119 of 130 for obstructions. 1671 loops so far!
# Checking row 120 of 130 for obstructions. 1679 loops so far!
# Checking row 121 of 130 for obstructions. 1680 loops so far!
# Checking row 122 of 130 for obstructions. 1699 loops so far!
# Checking row 123 of 130 for obstructions. 1700 loops so far!
# Checking row 124 of 130 for obstructions. 1700 loops so far!
# Checking row 125 of 130 for obstructions. 1700 loops so far!
# Checking row 126 of 130 for obstructions. 1703 loops so far!
# Checking row 127 of 130 for obstructions. 1704 loops so far!
# Checking row 128 of 130 for obstructions. 1705 loops so far!
# Checking row 129 of 130 for obstructions. 1705 loops so far!
# 1705