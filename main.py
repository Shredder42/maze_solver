from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    num_rows = 20
    num_cols = 20
    margin = 10
    screen_x = 800
    screen_y = 600
    cell_size_x = 20
    cell_size_y = 20

    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_cols, num_rows, cell_size_x, cell_size_y, win)
    print('maze created')

    is_solvable = maze.solve()
    if not is_solvable:
        print('maze cannot be solved!')
    else:
        print('maze solved!')

    win.wait_for_close()


if __name__ == '__main__':
    main()