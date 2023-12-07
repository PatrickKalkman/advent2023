import time


def read_input_file():
    with open("input2.txt", "r") as open_file:
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
            parts = line.replace("seeds: ", "").split()
            seeds = []
            for i in range(0, len(parts), 2):
                start = int(parts[i])
                range_length = int(parts[i + 1])
                seeds.extend(range(start, start + range_length))
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


def estimate_remaining_time(start_time, current_count, total_count):
    elapsed_time = time.time() - start_time
    time_per_item = elapsed_time / current_count
    remaining_time = time_per_item * (total_count - current_count)
    return remaining_time / 60  # Convert seconds to minutes



lines = read_input_file()
print("Generating seeds")
seeds = get_seeds(lines)
print(f"Number of seeds: {len(seeds)}")
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

start_time = time.time()
lowest_location = 2**63
number_of_seeds = len(seeds)
seed_count = 0

for seed in seeds:
    seed_count += 1
    location = map_seed_to_location(seed, mappings)
    if location < lowest_location:
        lowest_location = location

    # Progress update
    if seed_count % 100000 == 0 or seed_count == number_of_seeds:
        progress_percentage = (seed_count / number_of_seeds) * 100
        remaining_time = estimate_remaining_time(start_time, seed_count, number_of_seeds)
        print(f"Processed {seed_count} seeds ({progress_percentage:.2f}%) - Estimated time remaining: {remaining_time:.2f} minutes")



print(f"Lowest location is {lowest_location}")
