import helpers
import math
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()

# HEIGHT = 7 
# WIDTH = 11
# input = test_input

HEIGHT = 103
WIDTH = 101
input = my_input

SECONDS = 100

# p=9,5 v=-3,-3
def parse_input(input):
  robot_str = input.split("\n")
  robots = []
  for robot_str in robot_str:
    position_str = robot_str.split('p=')[1].split(' v=')[0]
    velocity_str = robot_str.split(' v=')[1]
    pos_str = position_str.split(',')
    vel_str = velocity_str.split(',')
    pos = (int(pos_str[0]), int(pos_str[1]))
    vel = (int(vel_str[0]), int(vel_str[1]))
    robots.append((pos, vel))
  return robots

def get_location_on_second(robot, sec):
  (pos, vel) = robot
  x = (pos[0] + vel[0] * sec) % WIDTH
  y = (pos[1] + vel[1] * sec) % HEIGHT
  return (x,y)

def print_locs(locs):
  for i in range(HEIGHT):
    row = ""
    for j in range(WIDTH):
      num = locs.count((j,i))
      char = '.' if num == 0 else str(num)
      row += char
    print(row)

def calculate_quadrants(locs):
  quads = [0,0,0,0]
  for loc in locs:
    if loc[0] < WIDTH//2 and loc[1] < HEIGHT//2:
      quads[0] += 1
    elif loc[0] > WIDTH//2 and loc[1] < HEIGHT//2:
      quads[1] += 1
    elif loc[0] < WIDTH//2 and loc[1] > HEIGHT//2:
      quads[2] += 1
    elif loc[0] > WIDTH//2 and loc[1] > HEIGHT//2:
      quads[3] += 1
  return quads

robots = parse_input(input)
START_RANGE = 0
END_RANGE = 100000
RANGE_SIZE = END_RANGE - START_RANGE

BOTTOM_ROW = math.floor(HEIGHT * .6)
MIDDLE = WIDTH//2
print(BOTTOM_ROW,MIDDLE)

def any_robots_touch_enough(locs):
  for loc in locs:
    if (loc[0],loc[1]+1) in locs and  (loc[0],loc[1]-1) in locs and   (loc[0]-1,loc[1]+1) in locs and   (loc[0]-1,loc[1]-1) in locs and (loc[0]+1,loc[1]+1) in locs and  (loc[0]+1,loc[1]-1) in locs:
      return True
  return False

for i in range(START_RANGE,END_RANGE):
  locs = []
  for robot in robots:
    loc = get_location_on_second(robot, i)
    locs.append(loc)
  if any_robots_touch_enough(locs):
    print(f"====={i}=====")
    print_locs(locs)
    print(f"====={i}=====")
  # quads = calculate_quadrants(locs)
  # quads[0] == quads[1] and quads[2] == quads[3] and quads[0] > quads[2]: #
  # if (MIDDLE-1, BOTTOM_ROW) in locs and (MIDDLE, BOTTOM_ROW) in locs and (MIDDLE+1,BOTTOM_ROW) in locs: # and (MIDDLE,BOTTOM_ROW+1) in locs:
  #   print_locs(locs)
  #   print("==========")
  if i % (RANGE_SIZE//10) == 0:
    print(f"============================== {i//(RANGE_SIZE//100)}% =======================================")
  
print('done')
# print_locs(locs)
# quads = calculate_quadrants(locs)
# print(quads)
# print('total',quads[0]*quads[1]*quads[2]*quads[3])
