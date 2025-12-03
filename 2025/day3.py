my_input_txt = open("./2025/my_input.txt", "r")
my_input = my_input_txt.read()

test_input_txt = open("./2025/test_input.txt", "r")
test_input = test_input_txt.read()


input = my_input

def find_biggest(bank, length):
  # print("finding biggest of", bank,"length",length)
  char_index = -1
  bank_to_check = bank if length == 1 else bank[:(-1*(length-1))]
  for i in range(0,10):
    # print("checking in ",bank_to_check)
    if str(i) in bank_to_check:
      char_index = bank.index(str(i))
  
  if length == 1:
    return bank[char_index]
  else:
    return bank[char_index]+find_biggest(bank[char_index+1:], length-1)



def solution():
  total = 0
  banks = input.split("\n")
  for bank in banks:
    # print(bank)
    biggest = int(find_biggest(bank,12))
    print(bank, biggest)
    total += biggest
  return total


print(solution())