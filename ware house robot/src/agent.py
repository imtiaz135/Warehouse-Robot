import numpy as np
import random

class QLearningAgent:
    def __init__(self, rows, cols):
        self.Q = np.zeros((rows, cols, 2, 4))
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 1.0

    def choose_action(self, state, has_item):
        r, c = state
        if random.uniform(0,1) < self.epsilon:
            return random.randint(0,3)
        return np.argmax(self.Q[r, c, int(has_item)])

    def update(self, state, action, reward, next_state, has_item, next_has_item):
        r, c = state
        nr, nc = next_state

        self.Q[r, c, int(has_item), action] += self.alpha * (
            reward + self.gamma * np.max(self.Q[nr, nc, int(next_has_item)])
            - self.Q[r, c, int(has_item), action]
        )

    def decay_epsilon(self):
        self.epsilon = max(0.01, self.epsilon * 0.995)