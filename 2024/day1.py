my_input_txt = open("./2024/my_input.txt", "r")
my_input = my_input_txt.read()

test_input_txt = open("./2024/test_input.txt", "r")
test_input = test_input_txt.read()

print(test_input)

first_list = []
second_list = []
test_input_lines= my_input.split("\n")
for line in test_input_lines:
  chars = line.split('   ')
  first_list.append(chars[0])
  second_list.append(chars[-1])

first_list.sort()
second_list.sort()

total = 0
for i in range(0, len(first_list)):
  total += abs(int(first_list[i]) - int(second_list[i]))

print('total', total)