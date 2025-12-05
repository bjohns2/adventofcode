my_input = open("./2025/my_input.txt", "r").read()
test_input = open("./2025/test_input.txt", "r").read()

input = my_input

def transform_range(string_range):
  return range(int(string_range.split('-')[0]),int(string_range.split('-')[1])+1)

def solution():
  inputs = input.split("\n\n")
  string_ranges = inputs[0].split("\n")
  ranges = [transform_range(r) for r in string_ranges]
  string_ingredients = inputs[1].split("\n")
  ingredients = [int(i) for i in string_ingredients]

  ranges.sort( key=lambda x: x[0])

  count = 0
  start = ranges[0][0]
  end = ranges[0][-1]+1
  for r in ranges:
    # print("looking at",r,', current run is',range(start,end))
    # if you start before the last one ends, continue it
    if r[0] <= end:
      end = max(r[-1]+1,end)
    # else, you start after the last one ends; need to count up the last one and start a new one
    else:
      # print("found range from",start,'to',end,', adding', end-start)
      count += (end-start)
      start = r[0]
      end = r[-1]+1
  # print("adding final range from",start,'to',end,', adding', end-start)
  count += (end-start)
  return count



print(solution())