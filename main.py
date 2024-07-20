import heapq
def get_blank_position(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j
    return None, None
def is_valid_position(x, y):
    return 0 <= x < 3 and 0 <= y < 3
def generate_new_state(puzzle, x1, y1, x2, y2):
    #  copy puzzle
    new_puzzle = [row[:] for row in puzzle]
    #  swap vị trí
    new_puzzle[x1][y1], new_puzzle[x2][y2] = new_puzzle[x2][y2], new_puzzle[x1][y1]
    return new_puzzle

# bottom, left, top, right
row_moves = [1, 0, -1, 0]
col_moves = [0, -1, 0, 1]
def get_possible_moves(puzzle):
    x, y = get_blank_position(puzzle)
    possible_moves = []
    for i in range(4):
        new_x, new_y = x + row_moves[i], y + col_moves[i]
        if is_valid_position(new_x, new_y):
            new_state = generate_new_state(puzzle, x, y, new_x, new_y)
            possible_moves.append(new_state)

    return possible_moves

def manhattan_distance(puzzle, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == puzzle[i][j]:
                            goal_x, goal_y = x, y
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def get_best_move(possible_moves, goal):
    best_move = None
    best_distance = float('inf')
    for move in possible_moves:
        distance = manhattan_distance(move, goal)
        if distance < best_distance:
            best_distance = distance
            best_move = move
    return best_move

def hill_climbing(initial, goal):
    current_state = initial
    current_distance = manhattan_distance(current_state, goal)
    steps = 0

    while True:
        possible_moves = get_possible_moves(current_state)
        best_move = get_best_move(possible_moves, goal)
        best_distance = manhattan_distance(best_move, goal)

        if best_distance >= current_distance:
            break

        current_state = best_move
        current_distance = best_distance
        steps += 1

        print(f"Step {steps}:")
        for row in current_state:
            print(row)
        print(f"Distance: {current_distance}")
        print()

    return current_state
def hill_climbing_with_backtracking(initial, goal):
    def recursive_hill_climbing(state, path, visited):
        path.append(state)
        visited.add(tuple(tuple(row) for row in state))
        if state == goal:
            return path
        possible_moves = get_possible_moves(state)
        best_move = get_best_move(possible_moves, goal)
        best_distance = manhattan_distance(best_move, goal)
        # print(f"Distance {manhattan_distance(state, goal)}:")
        # for row in state:
        #     print(row)
        # print()
        if best_distance < manhattan_distance(state, goal):
            # for row in best_move:
            #     print(row)
            # print()
            result = recursive_hill_climbing(best_move, path, visited)
            if result:
                return result
        # print(f"Distance {manhattan_distance(state, goal)}")
        # for row in state:
        #     print(row)
        # print()
        path.pop()
        return None

    path = []
    visited = set()
    solution_path = recursive_hill_climbing(initial, path, visited)

    if solution_path:
        for step, state in enumerate(solution_path):
            print(f"Step {step}:")
            for row in state:
                print(row)
            print(f"Distance: {manhattan_distance(state, goal)}")
            print()
        return solution_path[-1]
    else:
        # print("No solution found.")
        return None

def hill_climbing_with_priority(initial, goal):
    pq = []
    heapq.heappush(pq, (manhattan_distance(initial, goal), initial, []))
    visited = set()

    while pq:
        current_distance, current_state, path = heapq.heappop(pq)
        visited.add(tuple(tuple(row) for row in current_state))
        # print(f"Distance {current_distance}")
        # for row in current_state:
        #     print(row)
        # print()
        if current_state == goal:
            path.append(current_state)
            return path
        possible_moves = get_possible_moves(current_state)
        for move in possible_moves:
            move_tuple = tuple(tuple(row) for row in move)
            if move_tuple not in visited:
                heapq.heappush(pq, (manhattan_distance(move, goal), move,
                                    path + [current_state]))
    # print("No solution found.")
    return None

# Đề bài
# initial = [[2, 8, 3],
#            [1, 6, 4],
#            [7, 0, 5]]

# easy test
# initial = [[1, 3, 4],
#            [8, 2, 0],
#            [7, 6, 5]]

# backtrack
initial = [[8, 2, 3],
           [0, 6, 4],
           [7, 1, 5]]

# only priority
# initial = [[1, 0, 2],
#            [8, 3, 6],
#            [7, 4, 5]]


final = [[1, 2, 3],
         [8, 0, 4],
         [7, 6, 5]]



#

result = hill_climbing(initial, final)

print("Final state reached by hill climbing:")
for row in result:
    print(row)



result = get_possible_moves(initial)
for move in result:
    for row in move:
        print(row)
    print(f"Distance: {manhattan_distance(move, final)}")
    print()
#
# for puzzle in result:
#     print(manhattan_distance(puzzle,final))
# print()
#
# best_move = get_best_move(result,final)
# for row in best_move:
#     print(row)




# result = hill_climbing_with_backtracking(initial, final)
#
# print("Final state reached by hill climbing with backtracking:")
# if result:
#     for row in result:
#         print(row)
# else:
#     print("Solution not found.")


# result = hill_climbing_with_priority(initial, final)
# if result:
#     for step, state in enumerate(result):
#         print(f"Step {step}:")
#         for row in state:
#             print(row)
#         print(f"Distance: {manhattan_distance(state, final)}")
#         print()
# else:
#     print("Solution not found.")

