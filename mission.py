from collections import deque

# Define the initial and goal states
initial_state = (3, 2, 1)  # (Missionaries on left, Cannibals on left, Boat position)
goal_state = (0, 0, 0)

# Define the actions: (m, c) represents the number of missionaries and cannibals to move
actions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]


# Define a function to check if a state is valid
def is_valid(state):
    m_left, c_left, boat = state
    m_right, c_right = 3 - m_left, 3 - c_left

    if 0 <= m_left <= 3 and 0 <= c_left <= 3 and 0 <= m_right <= 3 and 0 <= c_right <= 3:
        if m_left == 0 or m_left >= c_left:
            if m_right == 0 or m_right >= c_right:
                return True
    return False

# Define a function to generate next valid states from the current state
def get_next_states(state):
    m, c, b = state
    next_states = []
    for action in actions:
        # print(action)
        if b == 1:  # Boat is on the left side
            new_state = (m - action[0], c - action[1], 0)
        else:  # Boat is on the right side
            new_state = (m + action[0], c + action[1], 1)
        if is_valid(new_state):
            next_states.append(new_state)
    return next_states

# Define BFS to find the solution
def bfs():
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        visited.add(state)
        state_list=get_next_states(state)
        for next_state in state_list:
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

# Solve the problem
solution = bfs()

# Print the solution
if solution:
    print("Solution found:")
    for i, state in enumerate(solution):
        m_left, c_left, b = state
        m_right, c_right = 3 - m_left, 3 - c_left
        print(f"Step {i + 1}: ({m_left}, {c_left}) { '<-' if b == 1 else '->'} ({m_right}, {c_right})")
else:
    print("No solution found.")
