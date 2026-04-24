from environment import *
from agent import QLearningAgent
from visualization import *
import matplotlib.pyplot as plt

agent = QLearningAgent(rows, cols)

start = (0,0)
from visualization import select_points

points = select_points(rows, cols, obstacles)

pickup = points[0]
drop = points[1]

print(f"Pickup: {pickup}, Drop: {drop}")

episodes = 2000
rewards = []

for ep in range(episodes):
    state = start
    has_item = False
    total_reward = 0

    for _ in range(100):
        action = agent.choose_action(state, has_item)
        next_state = get_next_state(state, action)

        next_has_item = has_item
        if next_state == pickup:
            next_has_item = True

        reward = get_reward(next_state, pickup, drop, has_item)

        agent.update(state, action, reward, next_state, has_item, next_has_item)

        state = next_state
        has_item = next_has_item
        total_reward += reward

        if state == drop and has_item:
            break

    rewards.append(total_reward)
    agent.decay_epsilon()

plot_rewards(rewards)

# Simulation
state = start
has_item = False

for _ in range(50):
    draw_grid(rows, cols, state, pickup, drop, obstacles, has_item)

    action = agent.choose_action(state, has_item)
    state = get_next_state(state, action)

    if state == pickup:
        has_item = True

    if state == drop and has_item:
        print("Task Completed!")
        break

plt.close()