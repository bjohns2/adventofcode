my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

available_towels = [i.strip() for i in input.split("\n")[0].split(',')]
designs = input.split("\n")[2:]

cache = {'': True}

print('available_towels',','.join(available_towels))
def check_design(design,available_towels):
  if design in cache:
    return cache[design]
  for towel in available_towels:
    towel_size = len(towel)
    if design[:towel_size] == towel:
      design_check = check_design(design[towel_size:],available_towels)
      if design_check:
        cache[design] = True
        return True
  cache[design] = False
  return False

total = 0
for design in designs:
  valid = check_design(design,available_towels)
  if valid:
    total +=1
  else:
    print(design,valid)
print(total)
