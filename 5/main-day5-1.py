
def read_input_file():
    with open("input1.txt", "r") as open_file:
        lines = open_file.readlines()

    return lines


def create_translation_map(mapping_data):
    translation_map = {}

    for line in mapping_data:
        parts = line.strip().split()
        if len(parts) != 3:
            continue

        dest_start, source_start, range_length = map(int, parts)
        source_end = source_start + range_length
        # Store the mapping as source range to destination start
        translation_map[(source_start, source_end)] = dest_start

    return translation_map


def translate_number(num, translation_map):
    for (source_start, source_end), dest_start in translation_map.items():
        if source_start <= num < source_end:
            offset = num - source_start
            return dest_start + offset
    return num


def get_seeds(lines):
    for line in lines:
        if line.startswith("seeds: "):
            line = line.replace("seeds: ", "")
            seeds = line.split()
            seeds = [int(seed) for seed in seeds]
            return seeds
    return []


def create_map(lines, start_token):
    mapping_data = []
    capture = False

    for line in lines:
        if start_token in line:
            capture = True
            continue

        if capture:
            if line.strip() == "" or "map:" in line:
                break
            mapping_data.append(line)

    return create_translation_map(mapping_data)


def map_seed_to_location(seed, mappings):
    for mapping in mappings:
        seed = translate_number(seed, mapping)
    return seed


lines = read_input_file()
seeds = get_seeds(lines)
seed_to_soil_map = create_map(lines, 'seed-to-soil map:')
soil_to_fertilizer_map = create_map(lines, 'soil-to-fertilizer map:')
fertilizer_to_water_map = create_map(lines, 'fertilizer-to-water map:')
water_to_light_map = create_map(lines, 'water-to-light map:')
light_to_temperature_map = create_map(lines, 'light-to-temperature map:')
temperature_to_humidity_map = create_map(lines, 'temperature-to-humidity map:')
humidity_to_location_map = create_map(lines, 'humidity-to-location map:')

mappings = [
    seed_to_soil_map,
    soil_to_fertilizer_map,
    fertilizer_to_water_map,
    water_to_light_map,
    light_to_temperature_map,
    temperature_to_humidity_map,
    humidity_to_location_map
]

# Process each seed through all mappings
lowest_location = 2**63
for seed in seeds:
    location = map_seed_to_location(seed, mappings)
    if location < lowest_location:
        lowest_location = location
    print(f"Seed {seed} maps to location {location}")

print(f"Lowest location is {lowest_location}")
