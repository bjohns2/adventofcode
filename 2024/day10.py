import helpers
import math
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

MAP_HEIGHT = len(input.split("\n"))
MAP_WIDTH = len(input.split("\n")[0])

print('MAP_HEIGHT',MAP_HEIGHT)
print('MAP_WIDTH',MAP_WIDTH)

def find_trailheads(map):
  trailheads = []
  for i,row in enumerate(map):
    for j,char in enumerate(row):
      if char == 0:
        trailheads.append([i,j])
  return trailheads

def is_valid(location):
  return location[0] >= 0 and location[1] >= 0 and location[0] < MAP_HEIGHT and location[1] < MAP_WIDTH

location_scores = {}

def trailhead_str(trailhead):
  # print(f"{trailhead[0]},{trailhead[1]}")
  return f"{trailhead[0]},{trailhead[1]}"  

def score_trailhead(trailhead, map):
  total_score = 0
  trailhead_score = map[trailhead[0]][trailhead[1]]
  if trailhead_str(trailhead) in location_scores:
    return location_scores[trailhead_str(trailhead)]
  if trailhead_score == 9:
    return 1
  up_trailhead = [trailhead[0]-1,trailhead[1]]
  if is_valid(up_trailhead) and map[up_trailhead[0]][up_trailhead[1]] == trailhead_score + 1:
   total_score += score_trailhead(up_trailhead, map)

  down_trailhead = [trailhead[0]+1,trailhead[1]]
  if is_valid(down_trailhead) and map[down_trailhead[0]][down_trailhead[1]] == trailhead_score + 1:
   total_score += score_trailhead(down_trailhead, map)

  left_trailhead = [trailhead[0],trailhead[1]-1]
  if is_valid(left_trailhead) and map[left_trailhead[0]][left_trailhead[1]] == trailhead_score + 1:
   total_score += score_trailhead(left_trailhead, map)

  right_trailhead = [trailhead[0],trailhead[1]+1]
  if is_valid(right_trailhead) and map[right_trailhead[0]][right_trailhead[1]] == trailhead_score + 1:
   total_score += score_trailhead(right_trailhead, map)

  location_scores[trailhead_str(trailhead)] = total_score
  return(total_score)




map = helpers.parse_int_map_from_input(input)
trailheads = find_trailheads(map)
total = 0
for trailhead in trailheads:
  total += score_trailhead(trailhead, map)
  # print(trailhead, score_trailhead(trailhead, map))
print(total)