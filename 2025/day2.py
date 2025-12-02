my_input_txt = open("./2025/my_input.txt", "r")
my_input = my_input_txt.read()

test_input_txt = open("./2025/test_input.txt", "r")
test_input = test_input_txt.read()


input = my_input

def is_invalid(num):
  snum = str(num)
  if len(snum) % 2 == 1:
    return False
  midpoint = len(snum)//2
  return snum[:midpoint] == snum[midpoint:]


invalids = 0
ranges = input.split(',')
for r in ranges:
  start = int(r.split('-')[0])
  end = int(r.split('-')[1])
  for num in range(start,end+1):
    if is_invalid(num):
      # print(num)
      invalids += num

print(invalids)




