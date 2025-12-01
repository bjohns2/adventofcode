my_input_txt = open("./2025/my_input.txt", "r")
my_input = my_input_txt.read()

test_input_txt = open("./2025/test_input.txt", "r")
test_input = test_input_txt.read()


input = my_input

position = 50
zero_count = 0
print('The dial starts by pointing at 50')
input_lines= input.split("\n")
for line in input_lines:
  right = line[0] == 'R'
  count = int(line[1:])
  if right:
    position = position + count
    # position = position % 100
    zeros_passed= position // 100
    if position  % 100 == 0:
      zeros_passed = max(0, zeros_passed-1)
  else:
    original_position = position
    position = position - count

    if original_position == 0:
       zeros_passed= max(abs(position // 100)-1,0)
    else:
       zeros_passed= abs(position // 100)


  zero_count +=zeros_passed
  position = position % 100
  if position == 0:
    zero_count += 1
  print('The dial is rotated',line,'to point at',position, '; during this rotation, it points at zero',zeros_passed,'times')


print('zero count: ', zero_count)
# 2852 is too low
# 6911 is too high
# 6772 is too low

