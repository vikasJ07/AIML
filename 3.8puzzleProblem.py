hooray="hooorrrayyy"

def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def move_up(state):
    i, j = find_blank(state)
    if i > 0:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        return new_state
    else:
        return None


def move_down(state):
    i, j = find_blank(state)
    if i < 2:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        return new_state
    else:
        return None


def move_left(state):
    i, j = find_blank(state)
    if j > 0:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        return new_state
    else:
        return None


def move_right(state):
    i, j = find_blank(state)
    if j < 2:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        return new_state
    else:
        return None


def calculate_heuristic(state, goal_state):
    
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                h += 1
    return h


def a_star(initial_state, goal_state):
   
    OPEN, CLOSED = [(calculate_heuristic(initial_state, goal_state), 0, initial_state)], set()
    
    while OPEN:
        
        f, g, current = min(OPEN)
        OPEN.remove((f, g, current)) 
        CLOSED.add(tuple(map(tuple, current)))  
        
        print_state(current) 
        print(" ")
        
        
        if current == goal_state:
            print(f"{hooray}Solution found!")
            return
        
        
        for move in [move_up, move_down, move_left, move_right]:
            successor = move(current)
            
            
            if successor and tuple(map(tuple, successor)) not in CLOSED:
                
                OPEN.append((g + 1 + calculate_heuristic(successor, goal_state), g + 1, successor))
    

    print(f"{hooray}No solution found.",)


initial_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

goal_state = [
    [2, 8, 1],
    [0, 4, 3],
    [7, 6, 5]
]

a_star(initial_state, goal_state)
