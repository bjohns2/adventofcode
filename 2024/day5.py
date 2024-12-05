import math
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

order_str = input.split("\n\n")[0]
update_str = input.split("\n\n")[1]

orders = order_str.split("\n")
updates = update_str.split("\n")

def is_ordered(update):
  for i in range(0,len(update)):
    for j in range(i,len(update)):
      if f"{update[j]}|{update[i]}" in orders:
        return False
  return True

ordered_updates = []
for update_str in updates:
  update = update_str.split(',')
  if is_ordered(update):
    ordered_updates.append(update)

total = 0
for update in ordered_updates:
  middle_num = update[math.floor(len(update)/2)]
  total += int(middle_num)
print(total)