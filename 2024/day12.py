import helpers
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

def build_region(regions, map, i, j, char):
  if i < 0 or j < 0 or i >= len(map) or j >= len(map[0]):
    return
  region = map[i][j]
  # print("looking at ",region,char)
  if region != char:
    return
  if region in regions and (i,j) in regions[region]:
    return
  if region not in regions:
    regions[region] = [(i,j)]
  else:
    regions[region].append((i,j))
  build_region(regions, map, i+1, j, char)
  build_region(regions, map, i-1, j, char)
  build_region(regions, map, i, j+1, char)
  build_region(regions, map, i, j-1, char)

def build_regions(map):
  all_regions = {}
  for i,row in enumerate(map):
    for j,char in enumerate(row):
      regions = {}
      build_region(regions, map, i, j, char)
      this_region = regions[char]
      if char not in all_regions:
        all_regions[char] = [this_region]
      elif this_region[0] not in helpers.flatten(all_regions[char]):
        all_regions[char].append(this_region)      
  return all_regions

def calculate_permiter(region):
  perimiter = set()
  for loc in region:
    perimiter.add((loc[0]+1,loc[1],'top'))
    perimiter.add((loc[0]-1,loc[1],'bottom'))
    perimiter.add((loc[0],loc[1]+1,'left'))
    perimiter.add((loc[0],loc[1]-1,'right'))
  for loc in region:
    for dir in ['top','bottom','left','right']:
      pos = (loc[0],loc[1],dir)
      if pos in perimiter:
        perimiter.remove(pos)
  return perimiter

total = 0
map = helpers.parse_map_from_input(input)
all_regions = build_regions(map)
for key in all_regions:
  for region in all_regions[key]:
    area = len(region)
    perimiter = len(calculate_permiter(region))
    print(key,":", area,perimiter)
    total += area * perimiter
print('total:',total)