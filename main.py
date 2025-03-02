from graphics import Window
from maze import Maze

def main():

    win_width = 800
    win_height = 600
    num_rows = 12
    num_cols = 16
    margin = 50
    cell_size_x = (win_width - 2 * margin) / num_cols
    cell_size_y = (win_height - 2 * margin) / num_rows

    win = Window(win_width, win_height)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)

    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()