my_input_txt = open("./2025/my_input.txt", "r")
my_input = my_input_txt.read()

test_input_txt = open("./2025/test_input.txt", "r")
test_input = test_input_txt.read()


input = my_input

def is_invalid(num):
  snum = str(num)

  if len(snum) % 1 == 0 and len(snum) >=2:
    all_same = True
    for i in range(len(snum)//1-1):
      all_same = all_same and (snum[i*1:i*1+1] == snum[i*1+1:i*1+2])
      # print(snum[i*2:i*2+2],snum[i*2+2:i*2+4],all_same)
    if all_same == True:
      # print('invalid on 1s')
      return True

  if len(snum) % 2 == 0 and len(snum) >=4:
    all_same = True
    for i in range(len(snum)//2-1):
      all_same = all_same and (snum[i*2:i*2+2] == snum[i*2+2:i*2+4])
      # print(snum[i*2:i*2+2],snum[i*2+2:i*2+4],all_same)
    if all_same == True:
      # print('invalid on 2s')
      return True
  
  if len(snum) % 3 == 0 and len(snum )>=6:
    all_same = True
    for i in range(len(snum)//3-1):
      all_same = all_same and (snum[i*3:i*3+3] == snum[i*3+3:i*3+6])
      # print(snum[i*3:i*3+3],snum[i*3+3:i*3+6],all_same)
    if all_same == True:
      return True
  
  if len(snum) % 4 == 0 and len(snum) >=8:
    all_same = True
    for i in range(len(snum)//4-1):
      all_same = all_same and (snum[i*4:i*4+4] == snum[i*4+4:i*4+8])
    if all_same == True:
      return True
  
  if len(snum) % 5 == 0 and len(snum) >=10:
    all_same = True
    for i in range(len(snum)//5-1):
      all_same = all_same and (snum[i*5:i*5+5] == snum[i*5+5:i*5+10])
    if all_same == True:
      return True
  
  return False

invalids = 0
ranges = input.split(',')
for r in ranges:
  start = int(r.split('-')[0])
  end = int(r.split('-')[1])
  for num in range(start,end+1):
    if is_invalid(num):
      # print(num)
      invalids += num

print(invalids)




