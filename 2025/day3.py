my_input_txt = open("./2025/my_input.txt", "r")
my_input = my_input_txt.read()

test_input_txt = open("./2025/test_input.txt", "r")
test_input = test_input_txt.read()


input = my_input

def find_biggest(bank):
  first_char_index = -1
  second_char_index = -1

  for i in range(0,10):
    if str(i) in bank[:-1]:
      first_char_index = bank.index(str(i))


  for i in range(0,10):
    # print(i, str(i) in bank[first_char_index+1:], second_char_index)
    if str(i) in bank[first_char_index+1:]:
      second_char_index = (bank[first_char_index+1:]).index(str(i)) + first_char_index + 1

  
  biggest = bank[first_char_index] + bank[second_char_index]
  return int(biggest)



def solution():
  total = 0
  banks = input.split("\n")
  biggest = find_biggest(banks[0])
  for bank in banks:
    print(bank)
    biggest = find_biggest(bank)
    # print(bank, biggest)
    total += biggest
  return total


print(solution())