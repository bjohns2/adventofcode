my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

reports = input.split("\n")

def calcuate_if_decreasing(levels):
  history = []
  if levels[1] > levels[0]:
    history.append('up')
  if levels[2] > levels[1]:
    history.append('up')
  if levels[3] > levels[2]:
    history.append('up')
  if len(history) > 1:
    return False
  else:
    return True

def check_if_safe(levels, try_removing = True):
  print(levels)
  decreasing = calcuate_if_decreasing(levels)

  for i in range(0,len(levels)-1):
    if decreasing:
      if levels[i] > levels[i+1] + 3:
        if try_removing:
          return check_if_safe(levels[:i] + levels[i+ 1:], False) or check_if_safe(levels[:i+1] + levels[i+1 + 1:], False)
        else:
          return False
      if levels[i] <= levels[i+1]:
        if try_removing:
          return check_if_safe(levels[:i] + levels[i+ 1:], False) or check_if_safe(levels[:i+1] + levels[i+1 + 1:], False)
        else:
          return False
    else: # increasing
      if levels[i] < levels[i+1] - 3:
        if try_removing:
          return check_if_safe(levels[:i] + levels[i+ 1:], False) or check_if_safe(levels[:i+1] + levels[i+1 + 1:], False)
        else:
          return False
      if levels[i] >= levels[i+1]:
        if try_removing:
          return check_if_safe(levels[:i] + levels[i+ 1:], False) or check_if_safe(levels[:i+1] + levels[i+1 + 1:], False)
        else:
          return False
  return True

safe = 0
for report in reports:
  levels = [int(i) for i in report.split(' ')]
  if check_if_safe(levels):
    print('SAFE  ', levels)
    safe += 1
  else:
    print('UNSAFE', levels)
print(safe)

# 300 is too low

# test_case = [67, 59, 58, 57, 56]
# print(check_if_safe(test_case))
