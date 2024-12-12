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

def calculate_permiter(region,map):
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
  simplfied_permiter = set()
  # print('simplfied_permiter',simplfied_permiter)
  for i in range(-1,len(map)+1):
    continuous = False
    # print('resetting continuous to false')
    for dir in ['top','bottom']:
      for j in range(-1,len(map[0])+1):
        if (i,j,dir) in perimiter:
          # print(f"top/bottom found ({i},{j},{dir}), continuous {continuous}")
          if not continuous:
            # print('adding and setting continuous to true ')
            continuous = True
            simplfied_permiter.add((i,j,dir))
        else:
          # print(f"top/bottom found ({i},{j},{dir}),setting continuous tofalse")
          continuous = False
  for j in range(-1,len(map[0])+1):
    continuous = False
    for dir in ['left','right']:
      for i in range(-1,len(map)+1):
        if (i,j,dir) in perimiter:
          # print(f"left/right found ({i},{j},{dir}), continuous {continuous}")
          if not continuous:
            continuous = True
            simplfied_permiter.add((i,j,dir))
        else:
          continuous = False
  # print(perimiter)
  # print('simplfied_permiter',simplfied_permiter)
  return simplfied_permiter

total = 0
map = helpers.parse_map_from_input(input)
all_regions = build_regions(map)
for key in all_regions:
  for region in all_regions[key]:
    area = len(region)
    print('=====',key,'=====')
    perimiter = len(calculate_permiter(region,map))
    print(key,":", area,perimiter)
    total += area * perimiter
print('total:',total)