from dataclasses import dataclass
from queue import PriorityQueue

grid = []
with open('input1.txt', 'r') as f:
    for line in f.readlines():
        grid.append(tuple(map(int, line.strip())))
n, m = len(grid), len(grid[0])
print(n, m)

@dataclass(frozen=True)
class Pos:
    row: int
    col: int
    def __add__(self, other):
        return Pos(row=self.row + other.row, col=self.col + other.col)
    def __sub__(self, other):
        return Pos(row=self.row - other.row, col=self.col - other.col)
    def __neg__(self):
        return Pos(row=-self.row, col=-self.col)
    def __lt__(self, other):
        return True
    def dist(self, other):
        # manhattan
        return abs(self.row - other.row) + abs(self.col - other.col)

# state described as (position, direction, chain length)
start_state = (Pos(0, 0), None, 1)
goal_pos = Pos(n-1, m-1)

def a_star(start_state, goal_pos, min_chain_before_turn, max_chain):
    def h(state):
        # heuristic uses manhattan distance
        return state[0].dist(goal_pos)

    def get_nbrs(state):
        pos, direction, chain_length = state
        for delta in (Pos(1, 0), Pos(0, 1), Pos(-1, 0), Pos(0, -1)):
            if direction is not None:
                if delta == -direction:
                    continue
                if delta == direction and chain_length == max_chain:
                    continue
                if delta not in (-direction, direction) and chain_length < min_chain_before_turn:
                    continue
            new_pos = pos + delta
            if not (0 <= new_pos.row < n and 0 <= new_pos.col < m):
                continue
            new_direction = delta
            if new_direction != direction:
                new_chain_length = 1
            else:
                new_chain_length = chain_length + 1
            yield new_pos, new_direction, new_chain_length

    q = PriorityQueue()
    dist = {start_state: 0}
    q.put((dist[start_state] + h(start_state), start_state))

    while not q.empty():
        f_dist, current_state = q.get()
        if current_state[0] == goal_pos:
            return dist[current_state]
        if f_dist > dist[current_state] + h(current_state):
            continue
        for nbr_state in get_nbrs(current_state):
            g_dist = dist[current_state] + grid[nbr_state[0].row][nbr_state[0].col]
            if nbr_state in dist and dist[nbr_state] <= g_dist:
                continue
            dist[nbr_state] = g_dist
            q.put((dist[nbr_state] + h(nbr_state), nbr_state))

# part 1
print(a_star(start_state, goal_pos, 0, 3))

# part 2
print(a_star(start_state, goal_pos, 4, 10))