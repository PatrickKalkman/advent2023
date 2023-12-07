import time
import concurrent.futures
import threading


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


def process_seed(seed):
    # Access the global mappings variable
    global mappings
    return map_seed_to_location(seed, mappings)


def update_progress_and_check_lowest_location(location, lock):
    global lowest_location, seed_count, start_time, number_of_seeds
    with lock:
        if location < lowest_location:
            lowest_location = location
        seed_count += 1
        if (seed_count % 100000) == 0:
            elapsed_time = time.time() - start_time
            percent_complete = seed_count / number_of_seeds
            remaining_time = (elapsed_time / percent_complete) - elapsed_time
            print(f"Processed {percent_complete * 100:.2f}% of seeds")
            print(f"Estimated time remaining: {remaining_time / 60:.2f} minutes")


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
lock = threading.Lock()


# Using ThreadPoolExecutor to process seeds in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit all seeds for processing
    print("Filling thread pool")
    future_to_seed = {executor.submit(process_seed, seed): seed for seed in seeds}
    print("Starting processing seeds")

    # As each seed is processed, update progress and check lowest location
    for future in concurrent.futures.as_completed(future_to_seed):
        seed = future_to_seed[future]
        try:
            location = future.result()
            update_progress_and_check_lowest_location(location, lock)
        except Exception as exc:
            print(f"Seed {seed} generated an exception: {exc}")

print(f"Lowest location is {lowest_location}")
