my_input_txt = open("./2025/my_input.txt", "r")
my_input = my_input_txt.read()

test_input_txt = open("./2025/test_input.txt", "r")
test_input = test_input_txt.read()

input = my_input

def is_valid(loc,map):
  return loc[0] >= 0 and loc[1] >= 0 and loc[0] < len(map) and loc[1] < len(map[0])

def count_adjacents(loc, rows):
  i = loc[0]
  j = loc[1]
  adjacents = 0
  if is_valid([i-1, j-1],rows) and rows[i-1][j-1] == '@':
    adjacents += 1
  if is_valid([i-1, j],rows) and rows[i-1][j] == '@':
    adjacents += 1
  if is_valid([i-1, j+1],rows) and rows[i-1][j+1] == '@':
    adjacents += 1
  if is_valid([i, j-1],rows) and rows[i][j-1] == '@':
    adjacents += 1
  if is_valid([i, j+1],rows) and rows[i][j+1] == '@':
    adjacents += 1
  if is_valid([i+1, j-1],rows) and rows[i+1][j-1] == '@':
    adjacents += 1
  if is_valid([i+1, j],rows) and rows[i+1][j] == '@':
    adjacents += 1
  if is_valid([i+1, j+1],rows) and rows[i+1][j+1] == '@':
    adjacents += 1
  return adjacents

def solution():
  total = 0
  rows = input.split("\n")
  for i,row in enumerate(rows):
    for j,char in enumerate(row):
      if char == '@':
        adjacents = count_adjacents([i,j], rows)
        total += 1 if adjacents < 4 else 0
  return total


print(solution())