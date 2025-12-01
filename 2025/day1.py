my_input_txt = open("./2025/my_input.txt", "r")
my_input = my_input_txt.read()

test_input_txt = open("./2025/test_input.txt", "r")
test_input = test_input_txt.read()


input = my_input

position = 50
zero_count = 0

input_lines= input.split("\n")
for line in input_lines:
  right = line[0] == 'R'
  count = int(line[1:])
  if right:
    position = (position + count)%100
  else:
    position = (position - count)%100
  zero_count += 1 if position == 0 else 0

print('zero count: ', zero_count)
  
