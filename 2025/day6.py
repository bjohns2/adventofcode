from collections import defaultdict

my_input = open("./2025/my_input.txt", "r").read()
test_input = open("./2025/test_input.txt", "r").read()


input = my_input

def solution():
  problems = defaultdict(list)
  lines = input.split("\n")
  for line in lines:
    problem_i = 0
    for element in line.split(' '):
      element = element.strip()
      if len(element) > 0: # clean up the leading empy chars for single digits:
        problems[problem_i].append(element)
        problem_i += 1

  total = 0
  for problem in problems.values():
    print
    numbers = [int(n) for n in problem[:-1]]
    operator = problem[-1]
    if operator == '+':
      problem_total = sum(numbers)
    else: # *
      problem_total = 1
      for num in numbers:
        problem_total *= num
    total += problem_total

  return total

print(solution())

# 8784864 is too low