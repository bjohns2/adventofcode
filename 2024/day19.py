my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

available_towels = [i.strip() for i in input.split("\n")[0].split(',')]
designs = input.split("\n")[2:]

cache = {'': 1}

print('available_towels',','.join(available_towels))
def check_design(design,available_towels):
  if design in cache:
    return cache[design]
  total_per_towels = 0
  for towel in available_towels:
    towel_size = len(towel)
    if design[:towel_size] == towel:
      design_check = check_design(design[towel_size:],available_towels)
      total_per_towels += design_check
      # if design_check:
      # cache[design] = design_check
      # return design_check
  cache[design] = total_per_towels
  return total_per_towels

total = 0
for design in designs:
  design_check = check_design(design,available_towels)
  total += design_check
  print(design,design_check)
print(total)
