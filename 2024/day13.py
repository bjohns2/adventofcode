import helpers
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

puzzle_strs = input.split("\n\n")

def parse_button_line(button_str):
  x = button_str.split('X+')[1].split(', ')[0]
  y = button_str.split('Y+')[1]
  return (int(x), int(y))

def parse_prize_line(prize_str):
  x = prize_str.split('X=')[1].split(', ')[0]
  y = prize_str.split('Y=')[1]
  return (int(x), int(y))

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


puzzles = parse_puzzle_strs(puzzle_strs)
total = 0
for puzzle in puzzles:
  total += solve_puzzle(puzzle)
  print(solve_puzzle(puzzle))
print('total',total)