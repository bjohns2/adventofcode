my_input = open("./2025/my_input.txt", "r").read()
test_input = open("./2025/test_input.txt", "r").read()

input = my_input

def make_point(x):
  return [int(i) for i in x.split(',')]

def solution():
  lines = input.split("\n")
  points = [make_point(x) for x in lines]
  max_size = 0
  for i in range(0,len(points)):
    for j in range(i+1,len(points)):
      area = (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1])+1)
      # print(f"points {points[i][0]},{points[i][1]} and {points[j][0]},{points[j][1]} have area {area}")
      max_size = max(area, max_size)
  return max_size


print(solution())
