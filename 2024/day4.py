my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

lines = input.split("\n")

def point_has_letter(i,j,letter):
  if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[0]):
    return False
  return lines[i][j] == letter

def xmases_from(i,j):
  point_xmases = 0
  #up
  if point_has_letter(i-1,j,'M') and point_has_letter(i-2,j,'A') and point_has_letter(i-3,j,'S'):
    point_xmases += 1
  #down
  if point_has_letter(i+1,j,'M') and point_has_letter(i+2,j,'A') and point_has_letter(i+3,j,'S'):
    point_xmases += 1
  #left
  if point_has_letter(i,j-1,'M') and point_has_letter(i,j-2,'A') and point_has_letter(i,j-3,'S'):
    point_xmases += 1
  #right
  if point_has_letter(i,j+1,'M') and point_has_letter(i,j+2,'A') and point_has_letter(i,j+3,'S'):
    point_xmases += 1
  # diagonal up/left
  if point_has_letter(i-1,j-1,'M') and point_has_letter(i-2,j-2,'A') and point_has_letter(i-3,j-3,'S'):
    point_xmases += 1
  # diagonal up/right
  if point_has_letter(i+1,j-1,'M') and point_has_letter(i+2,j-2,'A') and point_has_letter(i+3,j-3,'S'):
    point_xmases += 1
  # diagonal down/left
  if point_has_letter(i-1,j+1,'M') and point_has_letter(i-2,j+2,'A') and point_has_letter(i-3,j+3,'S'):
    point_xmases += 1
  # diagonal down/right
  if point_has_letter(i+1,j+1,'M') and point_has_letter(i+2,j+2,'A') and point_has_letter(i+3,j+3,'S'):
    point_xmases += 1
  return point_xmases

xmases = 0
for i,line in enumerate(lines):
  for j, char in enumerate(line):
    if char == 'X':
      xmases += xmases_from(i,j)
print(xmases)