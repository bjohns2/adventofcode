my_input = open("./2025/my_input.txt", "r").read()
test_input = open("./2025/test_input.txt", "r").read()

input = my_input

def transform_range(string_range):
  return range(int(string_range.split('-')[0]),int(string_range.split('-')[1])+1)

def solution():
  inputs = input.split("\n\n")
  string_ranges = inputs[0].split("\n")
  ranges = [transform_range(r) for r in string_ranges]
  ingredients = inputs[1].split("\n")

  count = 0
  for ingredient in ingredients:
    for range in ranges:
      if int(ingredient) in range:
        count +=1 
        break
  return count



print(solution())