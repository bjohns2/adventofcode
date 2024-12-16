import helpers
import copy
from collections import defaultdict
my_input = open("./2024/my_input.txt", "r").read()
test_input = open("./2024/test_input.txt", "r").read()
input = my_input

def find_char(map,target_char):
  for i,row in enumerate(map):
    for j,char in enumerate(row):
      if char == target_char:
        return (i,j)
      
def find_left(loc):
  x = loc[0]
  y = loc[1]
  dir = loc[2]
  if dir == 'left':
    return (x,y,'down')
  if dir == 'down':
    return (x,y,'right')
  if dir == 'right':
    return (x,y,'up')
  if dir == 'up':
    return (x,y,'left')
  
def find_right(loc):
  x = loc[0]
  y = loc[1]
  dir = loc[2]
  if dir == 'left':
    return (x,y,'up')
  if dir == 'up':
    return (x,y,'right')
  if dir == 'right':
    return (x,y,'down')
  if dir == 'down':
    return (x,y,'left')
  
def find_forward(loc):
  x = loc[0]
  y = loc[1]
  dir = loc[2]
  if dir == 'left':
    return (x,y-1,'left')
  if dir == 'up':
    return (x-1,y,'up')
  if dir == 'right':
    return (x,y+1,'right')
  if dir == 'down':
    return (x+1,y,'down')

def find_backward(loc):
  x = loc[0]
  y = loc[1]
  dir = loc[2]
  if dir == 'left':
    return (x,y+1,'left')
  if dir == 'up':
    return (x+1,y,'up')
  if dir == 'right':
    return (x,y-1,'right')
  if dir == 'down':
    return (x-1,y,'down')

def handle_next_step(map,queue,cache,loc,score):
  x = loc[0]
  y = loc[1]
  dir = loc[2]
  if map[x][y] == '#':
    return
  if cache[loc] <= score:
    return
  queue.append(loc)
  cache[loc] = score

map = helpers.parse_map_from_input(input)
start = find_char(map,'S')
end = find_char(map,'E')

start_loc = (start[0],start[1],'right')

queue = [start_loc]
cache = defaultdict(lambda:100000000000)
cache[start_loc] = 0


while len(queue) > 0:
  loc = queue.pop()
  left = find_left(loc)
  right = find_right(loc)
  forward = find_forward(loc)
  current_score = cache[loc]
  handle_next_step(map,queue,cache,left,current_score+1000)
  handle_next_step(map,queue,cache,right,current_score+1000)
  handle_next_step(map,queue,cache,forward,current_score+1)

print('end',end)
left_score = cache[(end[0],end[1],'left')]
right_score = cache[(end[0],end[1],'right')]
down_score = cache[(end[0],end[1],'down')]
up_score = cache[(end[0],end[1],'up')]
score = min(left_score, right_score, down_score, up_score)
print('score',score)

total_history = set()
def handle_next_step_taken(map,queue,cache,loc,score):
  x = loc[0]
  y = loc[1]
  if map[x][y] == '#':
    return
  if cache[loc] == score:
    mini_loc = (loc[0],loc[1])
    total_history.add(mini_loc)
    queue.append(loc)

queue = []


end_left = (end[0],end[1],'left')
end_right = (end[0],end[1],'right')
end_up = (end[0],end[1],'up')
end_down = (end[0],end[1],'down')

if left_score == score:
  queue.append(end_left)
if right_score == score:
  queue.append(end_right)
if down_score == score:
  queue.append(end_down)
if up_score == score:
  queue.append(end_up)


while len(queue) > 0:
  loc = queue.pop()
  left = find_left(loc)
  right = find_right(loc)
  forward = find_backward(loc)
  current_score = cache[loc]
  handle_next_step_taken(map,queue,cache,left,current_score-1000)
  handle_next_step_taken(map,queue,cache,right,current_score-1000)
  handle_next_step_taken(map,queue,cache,forward,current_score-1)

print(len(total_history))

print('RESULT:',len(total_history) +1)