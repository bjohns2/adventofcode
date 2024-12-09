import helpers
from collections import defaultdict

my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

map = helpers.parse_map_from_input(input)


def build_node_map(map):
  node_map = defaultdict(list)
  for i, row in enumerate(map):
    for j, char in enumerate(row):
      if char != '.':
        node_map[char].append([i,j])
  return node_map

node_map = build_node_map(map)

def is_within_map(map, x, y):
  return x >=0 and y >= 0 and x < len(map) and y < len(map[0])

all_nodes = set()
for locs in node_map.values():
  for i in range(len(locs)):
    for j in range(i+1, len(locs)):
      # print("loc", locs[i], 'x', locs[j])
      first_node_x = locs[i][0] + (locs[i][0] - locs[j][0])
      first_node_y = locs[i][1] + (locs[i][1] - locs[j][1])
      second_node_x = locs[j][0] + (locs[j][0] - locs[i][0])
      second_node_y = locs[j][1] + (locs[j][1] - locs[i][1])
      # print(first_node_x, first_node_y)
      # print(second_node_x, second_node_y)
      if is_within_map(map, first_node_x, first_node_y):
        all_nodes.add(f"({first_node_x},{first_node_y})")
      if is_within_map(map, second_node_x, second_node_y):
        all_nodes.add(f"({second_node_x},{second_node_y})")
print(len(all_nodes))