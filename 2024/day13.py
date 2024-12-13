import helpers
import numpy as np
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input
part_1 = False

puzzle_strs = input.split("\n\n")


def parse_button_line(button_str):
  x = button_str.split('X+')[1].split(', ')[0]
  y = button_str.split('Y+')[1]
  return (int(x), int(y))

def parse_prize_line(prize_str):
  x = prize_str.split('X=')[1].split(', ')[0]
  y = prize_str.split('Y=')[1]
  if part_1:
      return (int(x), int(y))
  else:
    return (int(x)+10000000000000, int(y)+10000000000000)

def parse_puzzle_str(puzzle_str):
  a_str = puzzle_str.split("\n")[0]
  b_str = puzzle_str.split("\n")[1]
  prize_str = puzzle_str.split("\n")[2]
  a = parse_button_line(a_str)
  b = parse_button_line(b_str)
  prize = parse_prize_line(prize_str)
  return (a,b,prize)

def parse_puzzle_strs(puzzle_strs):
  puzzles = []
  for puzzle_str in puzzle_strs:
    puzzles.append(parse_puzzle_str(puzzle_str))
  return puzzles

def solve_puzzle(puzzle):
  cheapest_solution = 5000
  for press_a in range(100):
    for press_b in range(100):
      can_get_to_x = press_a * puzzle[0][0] + press_b * puzzle[1][0] == puzzle[2][0]
      can_get_to_y = press_a * puzzle[0][1] + press_b * puzzle[1][1] == puzzle[2][1]
      if can_get_to_x and can_get_to_y:
        cheapest_solution = min(cheapest_solution, 3*press_a + 1*press_b)
  if cheapest_solution == 5000:
    return 0
  return cheapest_solution

def is_int(num):

  result = (round(num) - 0.0001) <= num <= round(num) + 0.0001
  print(num,'is int',result)
  return result

def solve_puzzle_np(puzzle):
  buttons = np.array([[puzzle[0][0], puzzle[1][0]],[puzzle[0][1], puzzle[1][1]]])
  prize = np.array([puzzle[2][0], puzzle[2][1]])
  np_solution = np.linalg.solve(buttons,prize)
  # print('np solution',np_solution)
  if is_int(np_solution[0]) and is_int(np_solution[1]):
    return int(3*round(np_solution[0]) + 1*round(np_solution[1]))
  else:
    return 0


puzzles = parse_puzzle_strs(puzzle_strs)
np_total = 0
total = 0
for puzzle in puzzles:
  # print('======')
  # print(puzzle)
  solution = solve_puzzle(puzzle)
  np_solution = solve_puzzle_np(puzzle)
  total += solution
  np_total += np_solution
  # if solution != np_solution:
    # print('==========')
    # print('MISMATCH')
    # print(puzzle)
    # print(solution,'vs',np_solution)
print('total',total)
print('np_total',np_total)

# 76876079916619 is too low
# 61406313840282 is too low