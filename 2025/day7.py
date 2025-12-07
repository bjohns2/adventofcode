my_input = open("./2025/my_input.txt", "r").read()
test_input = open("./2025/test_input.txt", "r").read()

input = my_input

cache = {}

def split_beam(pos, lines):
  if pos in cache:
    return cache[pos]
  else:
    if pos[0] == len(lines):
      result = 1
    elif lines[pos[0]][pos[1]] == '^': # split
      result = split_beam((pos[0]+1,pos[1]-1), lines) + split_beam((pos[0]+1,pos[1]+1), lines) #[(pos[0]+1,pos[1]-1),(pos[0]+1,pos[1]+1)])
    else:
      result = split_beam( (pos[0]+1,pos[1]), lines ) 
    cache[pos] = result
    return result


def solution():
  lines = input.split("\n")
  start = (0,lines[0].find("S"))
  total = split_beam(start, lines)
  return(total)

print(solution())
# print(splits)
