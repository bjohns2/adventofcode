
# def seed_to_soil_map
#   "50 98 2
# 52 50 48"
# end

# def soil_to_fertilizer_map 
#   "0 15 37
# 37 52 2
# 39 0 15"
# end

# def fertilizer_to_water_map
#    "49 53 8
# 0 11 42
# 42 0 7
# 57 7 4"
# end

# def water_to_light_map 
#   "88 18 7
# 18 25 70
# "
# end

# def light_to_temperature_map 
#   "45 77 23
# 81 45 19
# 68 64 13"
# end

# def temperature_to_humidity_map 
#   "0 69 1
# 1 0 69"
# end

# def humidity_to_location_map
#    "60 56 37
# 56 93 4"
# end
# seeds = "79 14 55 13"

seeds = "3136945476 509728956 1904897211 495273540 1186343315 66026055 1381149926 11379441 4060485949 190301545 444541979 351779229 1076140984 104902451 264807001 60556152 3676523418 44140882 3895155702 111080695"
seeds_v2 = [(3136945476...3136945476+509728956), (1904897211...1904897211+495273540), (1186343315...1186343315+66026055), (1381149926...1381149926+11379441), (4060485949...4060485949+190301545),(444541979...444541979+351779229),(1076140984...1076140984+104902451),(264807001...264807001+60556152), (3676523418...3676523418+44140882),(3895155702...3895155702+111080695)]

# seed-to-soil map:
# 50 98 2
# 52 50 48
# destination_start, source_start, range

# seed  soil
# 0     0
# 1     1
# ...   ...
# 48    48
# 49    49
# 50    52
# 51    53
# ...   ...
# 96    98
# 97    99
# 98    50
# 99    51

def convert_map_to_ranges(input_map)
  lines = input_map.split("\n")
  ranges = []
  lines.each do |line|
    elements = line.split(' ')
    destination_start = elements[0].to_i
    source_start = elements[1].to_i
    range = elements[2].to_i
    source_to_destination = [(source_start...source_start+range), (destination_start...destination_start+range)]
    ranges << source_to_destination
  end
  return ranges
end

# puts convert_map_to_ranges(seed_to_soil_map)

def convert_source_to_destination(source, source_to_destination_map)
  relevant_mapping = source_to_destination_map.find do |source_range, destination_range|
    source_range.include? source
  end
  if relevant_mapping
    relevant_mapping[1].first + (source - relevant_mapping[0].first)
  else
    source
  end
end

# puts convert_source_to_destination(51, convert_map_to_ranges(seed_to_soil_map))

def convert_sources_to_destination(sources, source_to_destination_map)
  sources.map{|source| convert_source_to_destination(source, source_to_destination_map) }
end

# puts convert_sources_to_destination(seeds.split(' ').map(&:to_i), convert_map_to_ranges(seed_to_soil_map))


def convert_seeds_to_location(seeds)
  soil = convert_sources_to_destination(seeds, convert_map_to_ranges(seed_to_soil_map))
  puts "converted to soil"
  fert = convert_sources_to_destination(soil, convert_map_to_ranges(soil_to_fertilizer_map))
  puts "converted to fert"
  water = convert_sources_to_destination(fert, convert_map_to_ranges(fertilizer_to_water_map))
  puts "converted to water"
  light = convert_sources_to_destination(water, convert_map_to_ranges(water_to_light_map))
  puts "converted to light"
  temp = convert_sources_to_destination(light, convert_map_to_ranges(light_to_temperature_map))
  puts "converted to temp"
  humidity = convert_sources_to_destination(temp, convert_map_to_ranges(temperature_to_humidity_map))
  puts "converted to humidity"
  location = convert_sources_to_destination(humidity, convert_map_to_ranges(humidity_to_location_map))
  location
end

# puts convert_seeds_to_location(seeds.split(' ').map(&:to_i)).join(',')

puts "starting seeds[9]"
puts convert_seeds_to_location(seeds_v2[9]).min

# seeds[0]: 69323688
# seeds[1]: 
# seeds[2]: 2221744254
# seeds[3]: 1747424143 # submitted; this answer is too high
# seeds[4]: 1826869889
# seeds[5]:  219649502 # submitted; this answer is too high
# seeds[6]: 3494092106
# seeds[7]:  475615938 # submitted; this answer is too high
# seeds[8]: 2727172076
# seeds[9]: 2285358106