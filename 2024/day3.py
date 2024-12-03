import re

my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input


pattern = r'mul\(\d{1,3},\d{1,3}\)'


def parse_match(match):
  first_num = match.split('(')[1].split(',')[0]
  second_num = match.split(')')[0].split(',')[1]
  return [int(first_num), int(second_num)]

total = 0
matches = re.findall(pattern, input) 
for match in matches:
  parsed_match = parse_match(match)
  total += parsed_match[0] * parsed_match[1]
print(total)