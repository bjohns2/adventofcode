from collections import defaultdict

my_input = open("./2025/my_input.txt", "r").read()
test_input = open("./2025/test_input.txt", "r").read()


input = my_input

def math_nums(operator, nums):
  if operator == '+':
    problem_total = sum(nums)
  else: # *
    problem_total = 1
    for num in nums:
      problem_total *= num
  return problem_total

def solution():
  total = 0
  lines = input.split("\n")
  operator = '+'
  nums = []
  for i in range(len(lines[0])):
    num = ''
    for line in lines:
      num += line[i]

    if num[-1] in ['+','*']:
      mathed =  math_nums(operator, nums) # math up the nums from the last batch
      total += mathed
      print('joined', nums, 'with',operator,'to get', mathed, ', total:',total)
      operator = num[-1]
      nums = []
      num = num[:-1]

    num = num.strip()
    if len(num) > 0:
      nums.append(int(num))
    # print(num)

  mathed =  math_nums(operator, nums) # math up the nums from the last batch
  total += mathed
  print('joined', nums, 'with',operator,'to get', mathed, ', total:',total)
  return total
      

print(solution())



















  # total = 0
  # for problem in problems.values():
  #   print(problem)
  #   numbers = [int(n) for n in problem[:-1]]
  #   operator = problem[-1]
  #   if operator == '+':
  #     problem_total = sum(numbers)
  #   else: # *
  #     problem_total = 1
  #     for num in numbers:
  #       problem_total *= num
  #   total += problem_total

  # return total


# 8784864 is too low