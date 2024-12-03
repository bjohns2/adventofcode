test_input = "2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"



class Solution
  def parse_input(input)
    input.split("\n").map{|l| l.split('')}
  end
  
  MAX_HEAT = 1000
  
  $current_min_heat_loss = 10000

  def step_beam(map, location, direction, steps, seen, total_heat_loss_so_far)
    return MAX_HEAT if seen.include?("#{location[0]},#{location[1]}")
    return MAX_HEAT if location[1] >= map[0].size

    seen += ["#{location[0]},#{location[1]}"]
    at_bottom_right =  (location[0] == map.size - 1) && (location[1] == map[0].size - 1)
    # puts "location: #{location[0]},#{location[1]}, seen #{seen.size}, looking for #{[map.size - 1,map[0].size - 1]}" if (location[0] > 9 && location[1] > 9)
    # puts "#{location[0]} == #{map.size - 1}: #{(location[0] == map.size - 1)}"
    # puts "#{location[1]} == #{map[0].size - 1}: #{(location[0] == map.size - 1)}"
    heat_loss = map[location[0]][location[1]].to_i
    new_total = total_heat_loss_so_far + heat_loss
    return MAX_HEAT if new_total >= $current_min_heat_loss
    $current_min_heat_loss = new_total if at_bottom_right && (new_total < $current_min_heat_loss)
    puts "found bottom right, total heat loss #{new_total}, seen #{seen.size}, new low #{$current_min_heat_loss}" if at_bottom_right
    return heat_loss if at_bottom_right
    if direction == 'right'
      new_location = [location[0], location[1] + 1]
      return MAX_HEAT if location[1] + 1 >= map[0].size

      down = step_beam(map,  [location[0]+1, location[1]], 'down', 0, seen, new_total)
      up = step_beam(map, [location[0]-1, location[1]], 'up', 0, seen, new_total)

      if steps >= 2
        return [up , down].min + heat_loss
      else 
        right = step_beam(map,  [location[0], location[1]+1], 'right', steps + 1, seen, new_total)
        return [up, down, right].min + heat_loss
      end

    elsif direction == 'left'
      new_location = [location[0], location[1] - 1]
      return MAX_HEAT if location[1] - 1 < 0

      down = step_beam(map,  [location[0]+1, location[1]], 'down', 0, seen, new_total)
      up = step_beam(map, [location[0]-1, location[1]], 'up', 0, seen, new_total)
      
      if steps >= 2
        return [up , down].min + heat_loss
      else 
        left = step_beam(map,  [location[0], location[1]+1], 'left', steps + 1, seen, new_total)
        return [up, down, left].min + heat_loss
      end
    
    elsif direction == 'up'
      new_location = [location[0] - 1, location[1]]
      return MAX_HEAT if location[0] - 1 < 0

      right = step_beam(map,  [location[0], location[1]+1], 'right', 0, seen, new_total)
      left = step_beam(map,  [location[0], location[1]+1], 'left', 0, seen, new_total)

      if steps >= 2
        return [left, right].min + heat_loss
      else 
        up = step_beam(map, [location[0]-1, location[1]], 'up', steps + 1, seen, new_total)
        return [left, right, up].min + heat_loss
      end
      
    elsif direction == 'down'
      new_location = [location[0] + 1, location[1]]
      return MAX_HEAT if location[0] + 1 >= map.size

      right = step_beam(map,  [location[0], location[1]+1], 'right', 0, seen, new_total)
      left = step_beam(map,  [location[0], location[1]+1], 'left', 0, seen, new_total)

      if steps >= 2
        return [left, right].min + heat_loss
      else 
        down = step_beam(map,  [location[0]+1, location[1]], 'down', steps + 1, seen, new_total)
        return [left, right, down].min + heat_loss
      end
      
    end
  end

  def solution(input)
    map = parse_input(input)
    start_location = [0,0]
    seen = []
    puts step_beam(map, start_location, 'right', 0, seen, 0)
    puts step_beam(map, start_location, 'down', 0, seen, 0)
  end
end

Solution.new.solution(test_input)
# 1000 is too low