
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
  fert = convert_sources_to_destination(soil, convert_map_to_ranges(soil_to_fertilizer_map))
  water = convert_sources_to_destination(fert, convert_map_to_ranges(fertilizer_to_water_map))
  light = convert_sources_to_destination(water, convert_map_to_ranges(water_to_light_map))
  temp = convert_sources_to_destination(light, convert_map_to_ranges(light_to_temperature_map))
  humidity = convert_sources_to_destination(temp, convert_map_to_ranges(temperature_to_humidity_map))
  location = convert_sources_to_destination(humidity, convert_map_to_ranges(humidity_to_location_map))
  location
end

puts convert_seeds_to_location(seeds.split(' ').map(&:to_i)).join(',')

puts convert_seeds_to_location(seeds.split(' ').map(&:to_i)).min