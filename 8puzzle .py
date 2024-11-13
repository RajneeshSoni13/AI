import heapq
import time

# Goal configuration for the 8-puzzle
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Defining the moves (up, down, left, right)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row, col) directions

# Manhattan Distance Heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] == 0:
            continue
        goal_pos = GOAL_STATE.index(state[i])
        # Calculate the target row and column
        target_row, target_col = divmod(goal_pos, 3)
        current_row, current_col = divmod(i, 3)
        distance += abs(target_row - current_row) + abs(target_col - current_col)
    return distance

# Find the possible moves for the empty space
def get_possible_moves(state):
    empty_pos = state.index(0)
    row, col = divmod(empty_pos, 3)
    
    possible_moves = []
    for move in MOVES:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            # Swap the empty space with the tile at the new position
            new_state = state[:]
            new_state[empty_pos], new_state[new_pos] = new_state[new_pos], new_state[empty_pos]
            possible_moves.append((new_state, new_pos))
    return possible_moves

# A* Search algorithm to solve the 8-puzzle
def a_star_search(start_state):
    # Priority queue to store states with f(n) = g(n) + h(n)
    open_list = []
    heapq.heappush(open_list, (0 + manhattan_distance(start_state), 0, start_state, None, None))  # f(n), g(n), state, parent state, move
    
    # Set to keep track of visited states
    visited = set()
    visited.add(tuple(start_state))
    
    # Track the moves to reconstruct the path later
    came_from = {}
    
    while open_list:
        _, g, current_state, parent_state, move = heapq.heappop(open_list)
        
        # If goal state is reached, reconstruct the path
        if current_state == GOAL_STATE:
            path = []
            while current_state is not None:
                path.append((current_state, move))
                current_state, move = came_from.get(tuple(current_state), (None, None))
            path.reverse()
            return path
        
        # Get possible moves
        for new_state, new_pos in get_possible_moves(current_state):
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                h = manhattan_distance(new_state)
                f = g + 1 + h  # f(n) = g(n) + h(n)
                heapq.heappush(open_list, (f, g + 1, new_state, current_state, new_pos))
                came_from[tuple(new_state)] = (current_state, new_pos)
    
    return None  # No solution found

# Function to print the state in a 3x3 grid format
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

# Main function to execute the A* search
def solve_8_puzzle(start_state):
    print("Initial State:")
    print_state(start_state)
    
    start_time = time.time()
    solution = a_star_search(start_state)
    
    if solution:
        print("\nSolution found in", time.time() - start_time, "seconds")
        print("\nSteps to solve:")
        for state, move in solution:
            print_state(state)
            print()
    else:
        print("No solution found.")

# Example Start State (you can customize this)
start_state = [1, 2, 3, 4, 5, 6, 7, 0, 8]  # This is a simple example that is solvable

# Solve the puzzle
solve_8_puzzle(start_state)

