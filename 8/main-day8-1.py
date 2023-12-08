def read_input_file():
    with open("input1.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines


def parse_instructions(lines):
    return list(lines[0].strip())


def parse_graph(lines):
    graph = {}

    for line in lines:
        if "=" in line:  # Check if the line contains a graph definition
            parts = line.split("=")
            node = parts[0].strip()
            edges = parts[1].strip(" ()\n").split(", ")
            graph[node] = edges

    return graph


def navigate_graph(graph, instructions):
    current_node = "AAA"
    path = [current_node]

    while current_node != "ZZZ":
        for direction in instructions:
            if direction == 'L':
                current_node = graph[current_node][0]
            elif direction == 'R':
                current_node = graph[current_node][1]
            path.append(current_node)

            # Break out of the inner loop if "ZZZ" is reached
            if current_node == "ZZZ":
                break

    return path


lines = read_input_file()
graph = parse_graph(lines)
instructions = parse_instructions(lines)
path_taken = navigate_graph(graph, instructions)
print("Path taken:", path_taken)
print("Steps: ", len(path_taken) - 1)
