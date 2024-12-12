def parse_map_from_input(input):
  return input.split("\n")

def parse_int_map_from_input(input):
  return [[int(i) for i in suba] for suba in input.split("\n")]

def print_map(map):
  map_str = ""
  for row in map:
    map_str = map_str + "\n" +  row
  print(map_str)

def flatten(xss):
    return [x for xs in xss for x in xs]