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
  new_total = -1
  rows = input.split("\n")
  while total != new_total:
    # print(total, new_total)
    # print(("\n").join(rows))
    new_total = total
    new_rows = []
    for i,row in enumerate(rows):
      new_row = ''
      for j,char in enumerate(row):
        if char == '@':
          adjacents = count_adjacents([i,j], rows)
          if adjacents < 4:
            total += 1 
            new_row = new_row + '.'
          else:
            new_row = new_row + '@'
        else:
          new_row = new_row + '.'
      # print(new_row)
      new_rows.append(new_row)
    rows = new_rows
  return total


print(solution())