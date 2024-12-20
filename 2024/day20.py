import copy
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input
from collections import defaultdict


def find_char(map,target_char):
  for i,row in enumerate(map):
    for j,char in enumerate(row):
      if char == target_char:
        return (i,j)


def is_valid(loc,map):
  return loc[0] >= 0 and loc[1] >= 0 and loc[0] < len(map) and loc[1] < len(map[0])


def handle_step(map,queue,weights,loc,weight):
  i = loc[0]
  j = loc[1]
  if not is_valid(loc,map) or map[i][j] == '#':
    return
  if loc in weights and weights[loc] <= weight:
    return
  queue.append(loc)
  weights[loc] = weight

      
def solve_map(map,start,end):
  weights = {start:0}
  queue = [start]
  while len(queue) > 0:
    loc = queue.pop()
    left = (loc[0],loc[1]+1)
    right = (loc[0],loc[1]-1)
    up = (loc[0]-1,loc[1])
    down = (loc[0]+1,loc[1])
    loc_weight = weights[loc]
    handle_step(map,queue,weights,left,loc_weight+1)
    handle_step(map,queue,weights,right,loc_weight+1)
    handle_step(map,queue,weights,up,loc_weight+1)
    handle_step(map,queue,weights,down,loc_weight+1)
  return weights

input_map = [list(i) for i in input.split("\n")]
start = find_char(input_map, 'S')
end = find_char(input_map, 'E')
initial_weights = solve_map(input_map,start,end)
initial_score = initial_weights[end]
print('initial_score',initial_score)

def handle_adjacency(map,loc,cheats_to_try):
  if map[loc[0]][loc[1]] == '#':
    if [loc] not in cheats_to_try:
      cheats_to_try.append([loc])
    left = (loc[0],loc[1]+1)
    right = (loc[0],loc[1]-1)
    up = (loc[0]-1,loc[1])
    down = (loc[0]+1,loc[1])
    # if is_valid(left,map) and map[left[0]][left[1]] != '#':
    #   if [loc,left] not in cheats_to_try:
    #     cheats_to_try.append([loc,left])
    # if is_valid(right,map) and map[right[0]][right[1]] != '#':
    #   if [loc,right] not in cheats_to_try:
    #     cheats_to_try.append([loc,right])
    # if is_valid(up,map) and map[up[0]][up[1]] != '#':
    #   if [loc,up] not in cheats_to_try:
    #     cheats_to_try.append([loc,up])
    # if is_valid(down,map) and map[down[0]][down[1]] != '#':
    #   if [loc,down] not in cheats_to_try:
    #     cheats_to_try.append([loc,down])

answers = defaultdict(lambda:0)
cheats_to_try = []
total = 0
for loc in initial_weights:
    left = (loc[0],loc[1]+1)
    right = (loc[0],loc[1]-1)
    up = (loc[0]-1,loc[1])
    down = (loc[0]+1,loc[1])
    handle_adjacency(input_map,left,cheats_to_try)
    handle_adjacency(input_map,right,cheats_to_try)
    handle_adjacency(input_map,up,cheats_to_try)
    handle_adjacency(input_map,down,cheats_to_try)
# uniq_cheats = list(set(cheats_to_try))
for i,cheat in enumerate(cheats_to_try):
  # print(cheat)
  if i %100 == 0:
    print(i,'/',len(cheats_to_try))
  copied_map = copy.deepcopy(input_map)
  for loc in cheat:
    copied_map[loc[0]][loc[1]] = '.'
  new_weight = solve_map(copied_map,start,end)
  result = initial_score - new_weight[end]
  # print(new_weight[end])
  if result > 0:
    answers[result] += 1
  if result >= 100:
    total += 1
print(answers)
for key in sorted(list(answers.keys())):
  print('There are',answers[key],'cheats that save',key,'seconds')
print(total)