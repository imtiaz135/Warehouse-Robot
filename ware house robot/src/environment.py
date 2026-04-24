import numpy as np

rows, cols = 6, 6
obstacles = [(1,1), (1,2), (2,1), (3,3), (4,3)]

def get_next_state(state, action):
    r, c = state

    if action == 0: r -= 1
    elif action == 1: r += 1
    elif action == 2: c -= 1
    elif action == 3: c += 1

    r = max(0, min(rows-1, r))
    c = max(0, min(cols-1, c))

    if (r, c) in obstacles:
        return state

    return (r, c)

def get_reward(state, pickup, drop, has_item):
    if state == pickup and not has_item:
        return 20
    elif state == drop and has_item:
        return 50
    return -1