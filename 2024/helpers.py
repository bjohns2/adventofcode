def parse_map_from_input(input):
  return input.split("\n")

def print_map(map):
  map_str = ""
  for row in map:
    map_str = map_str + "\n" +  row
  print(map_str)