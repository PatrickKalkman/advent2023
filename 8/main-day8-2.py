from math import gcd
from functools import reduce


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def calculate_lcm(numbers):
    return reduce(lcm, numbers, 1)


def read_input_file():
    with open("input2.txt", "r") as open_file:
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


def find_start_nodes(graph):
    return [node for node in graph if node.endswith('A')]


def navigate_graph(graph, instructions, start_nodes):
    current_nodes = start_nodes.copy()

    result = []

    for node in current_nodes:
        total_steps = 0
        new_node = node
        while not new_node.endswith("Z"):
            for direction in instructions:
                total_steps += 1

                if direction == 'L':
                    new_node = graph[new_node][0]
                elif direction == 'R':
                    new_node = graph[new_node][1]

                if new_node.endswith("Z"):
                    result.append(total_steps)
                    print(new_node, total_steps)
                    break

    return result


lines = read_input_file()
graph = parse_graph(lines)
instructions = parse_instructions(lines)
start_nodes = find_start_nodes(graph)
total_steps = navigate_graph(graph, instructions, start_nodes)
result = calculate_lcm(total_steps)
print(result)
