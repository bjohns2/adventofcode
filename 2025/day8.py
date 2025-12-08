import math

my_input = open("./2025/my_input.txt", "r").read()
test_input = open("./2025/test_input.txt", "r").read()

input = my_input

def calc_distance(j1, j2):
  sum_of_squares = (j1[0] - j2[0])**2 + (j1[1] - j2[1])**2 + (j1[2] - j2[2])**2
  return math.sqrt(abs(sum_of_squares)  )

# print(calc_distance([162,817,812],[425,690,689]))


def solution():
  junctions = []
  for line in input.split("\n"):
    junction = []
    for num in line.split(","):
      junction.append(int(num))
    junctions.append(junction)
  connections = []
  for i in range(len(junctions)):
    for j in range (i+1,len(junctions)):
      distance = calc_distance(junctions[i], junctions[j])
      connections.append([distance, i,j])
  sorted_connections = sorted(connections, key=lambda item: item[0])
  circuits = [[n] for n in range(len(junctions))]
  # print('circuits start')
  # print(circuits)
  # print('connecitons')
  for connection in sorted_connections: 
    # print(connection) # distance, loc 1, loc 2
    new_circuits = []
    i_circuit = None
    j_circuit = None
    for circuit in circuits:
      if connection[1] in circuit:
        i_circuit = circuit or i_circuit
      if connection[2] in circuit:
        j_circuit = circuit or j_circuit
      if connection[1] not in circuit and connection[2] not in circuit:
        new_circuits.append(circuit)
    # print("for connection",connection,"found circuits",i_circuit,'and',j_circuit)
    # print('i',i_circuit, 'j',j_circuit, 'c1',connection[1], 'c2', connection[2])
    if i_circuit == j_circuit == None:
      raise Exception('how could there be none')
    elif i_circuit == j_circuit:
      new_circuits.append(i_circuit)
    else:
      new_circuits.append(i_circuit + j_circuit)
    circuits = new_circuits
    if len(circuits) == 1:
      print('last connection made:', connection, 'from', junctions[connection[1]], 'to', junctions[connection[2]])
      print('mulitplying',junctions[connection[1]][0] ,'*',  junctions[connection[2]][0])
      return(junctions[connection[1]][0] *  junctions[connection[2]][0])
  #   for c in circuits:
  #     print(c)
  # print('circuits when done')

  sorted_circuits = sorted(circuits, key=lambda i: -1*len(i))
  for c in sorted_circuits:
    print(c)
  
  # return(len(sorted_circuits[0])*len(sorted_circuits[1])*len(sorted_circuits[2]))


print(solution())

# 12 is wrong RIP -- 1000 PAIRS UGH