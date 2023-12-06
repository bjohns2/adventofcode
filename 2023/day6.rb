input = "Time:        35     69     68     87
Distance:   213   1168   1086   1248"

# input_formatted = [[35,213], [69,1169], [68,1086], [87,1248]]
input_formatted = [[35696887,213116810861248]]

all_winning_ways = 1
input_formatted.each do |race|
  time = race[0]
  distance = race[1]

  winning_ways = 0

  (1..time).each do |acceleration_time|
    winning_ways += 1 if acceleration_time * (time-acceleration_time) > distance
  end
  puts "race #{race}: can win #{winning_ways} different ways"
  all_winning_ways *= winning_ways
end
puts all_winning_ways