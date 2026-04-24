import matplotlib.pyplot as plt
import numpy as np

def plot_rewards(rewards):
    plt.plot(rewards)
    plt.title("Learning Progress")
    plt.xlabel("Episodes")
    plt.ylabel("Reward")
    plt.show()

def draw_grid(rows, cols, state, pickup, drop, obstacles, has_item):
    grid = np.ones((rows, cols, 3))

    for (r,c) in obstacles:
        grid[r][c] = [0,0,0]

    grid[pickup] = [1,1,0]
    grid[drop] = [0,1,0]

    r, c = state
    grid[r][c] = [0,0,1] if has_item else [1,0,0]

    plt.imshow(grid)
    plt.grid(True)
    plt.pause(0.4)
    plt.clf()

def select_points(rows, cols, obstacles):
    import matplotlib.pyplot as plt
    import numpy as np

    selected_points = []

    def onclick(event):
        if event.xdata is not None and event.ydata is not None:
            col = int(event.xdata)
            row = int(event.ydata)

            if (row, col) in obstacles:
                print("Cannot select obstacle!")
                return

            if len(selected_points) < 2:
                selected_points.append((row, col))
                print(f"Selected: {row, col}")
                plt.scatter(col, row, c='red', s=100)
                plt.draw()

            if len(selected_points) == 2:
                plt.close()

    fig, ax = plt.subplots()
    grid = np.ones((rows, cols, 3))

    for (r, c) in obstacles:
        grid[r][c] = [0, 0, 0]

    ax.imshow(grid)
    ax.set_title("Click Pickup then Drop")

    ax.set_xticks(np.arange(-.5, cols, 1))
    ax.set_yticks(np.arange(-.5, rows, 1))
    ax.grid(True)

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

    return selected_points