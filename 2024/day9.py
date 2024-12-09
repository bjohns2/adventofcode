import helpers

my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

my_list = []
file_index = 0
for i,char in enumerate(input):
  if i%2 == 0: # value
    for j in range(int(char)):
      my_list.append(file_index)
    file_index += 1
  else:
    for j in range(int(char)):
      my_list.append(None)

while None in my_list:
  v = my_list.pop()
  my_list[my_list.index(None)] = v

# print(my_list)

def checksum(l):
  total = 0
  for i in range(len(l)):
    total += i*l[i]
  return total

print(checksum(my_list))