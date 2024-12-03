my_input_txt = open("./2024/my_input.txt", "r")
my_input = my_input_txt.read()

test_input_txt = open("./2024/test_input.txt", "r")
test_input = test_input_txt.read()


input = my_input

first_list = []
second_list = []
input_lines= input.split("\n")
for line in input_lines:
  chars = line.split('   ')
  first_list.append(chars[0])
  second_list.append(chars[-1])

# first_list.sort()
# second_list.sort()

total = 0
for i in range(0, len(first_list)):
  total += abs(int(first_list[i]) * second_list.count(first_list[i]))

# apperances = {}


print('total', total)