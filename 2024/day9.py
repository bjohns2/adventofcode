import helpers
import math
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

# print(input)

int_input = [int(i) for i in input]
# print(int_input)
length = math.floor(len(input)/2)
# print(length)

# file_index = length
# for i in range(len(input) - 1, -1, -1):
#     print(i)
#     if i%2 == 0: # value
#       file_num = int(i/2)
#       print("looking to file",file_num,'at',i)

#       for j,char in enumerate(int_input):
#         if j%2 == 1 and j >= int_input[i]:
#           print('can put it earlier at',j)
#           int_input[j] = int_input[j] - int_input[i]
#           del int_input[i]
#           int_input.insert(j,char)
#           break
# print(int_input)
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

# print(my_list)

# while None in my_list:
#   v = my_list.pop()
#   my_list[my_list.index(None)] = v

for i in range(len(input) - 1, -1, -2):
    file_num = int(i/2)
    # print(my_list)
    # print(file_num)
    num_to_move = my_list.count(file_num)
    old_loc = my_list.index(file_num)

    for c,char in enumerate(my_list):
      # print("c+num_to_move",c+num_to_move,'my_list[c:c+num_to_move]',my_list[c:c+num_to_move])
      if c+num_to_move < len(my_list) and c < old_loc and my_list[c:c+num_to_move].count(None) == num_to_move:
        # print('can put',file_num,'at',c,'from',old_loc)
        for j in range(0,num_to_move):
          my_list[c+j] = file_num
          my_list[old_loc+j] = None
        break

# print(my_list)

def checksum(l):
  total = 0
  for i in range(len(l)):
    if l[i] != None:
      total += i*l[i]
  return total

print(checksum(my_list))