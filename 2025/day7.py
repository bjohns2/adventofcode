my_input = open("./2025/my_input.txt", "r").read()
test_input = open("./2025/test_input.txt", "r").read()

input = my_input

splits = 0

def split_beam(pos, line):
  global splits
  if line[pos[1]] == '^': # split
    splits += 1
    return([(pos[0]+1,pos[1]-1),(pos[0]+1,pos[1]+1)])
  else:
    return [(pos[0]+1, pos[1])]


def solution():
  lines = input.split("\n")
  start = (0,lines[0].find("S"))
  current_positions = [start]
  for i in range(1,len(lines)):
    print(i,current_positions)
    new_positions = []
    for pos in current_positions:
      new_positions += split_beam(pos, lines[i])
    current_positions = list(set(new_positions))
  return(len(current_positions)-1)

print(solution())
print(splits)
