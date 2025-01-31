from cell import Cell
import time
import random

class Maze():
    def __init__(
            self, 
            x1, 
            y1, 
            num_rows, 
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win=None,
            seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        upper_left_x = self._x1 + i * self._cell_size_x
        upper_left_y = self._y1 + j * self._cell_size_y
        lower_right_x = upper_left_x + self._cell_size_x
        lower_right_y = upper_left_y + self._cell_size_y
        self._cells[i][j].draw(upper_left_x, upper_left_y, lower_right_x, lower_right_y)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            to_visit = []
            left_col = i - 1
            above_row = j - 1
            right_col = i + 1          
            beneath_row = j + 1
            if left_col >= 0 and not self._cells[left_col][j].visited:
                to_visit.append((left_col, j))
            if above_row >= 0 and not self._cells[i][above_row].visited:
                to_visit.append((i, above_row))
            if right_col < self._num_cols and not self._cells[right_col][j].visited:
                to_visit.append((right_col, j))
            if beneath_row < self._num_rows and not self._cells[i][beneath_row].visited:
                to_visit.append((i, beneath_row))

            # if there is nowhere to go then break out
            if not to_visit:
                self._draw_cell(i, j)
                return
            # knock out walls between this cell and next cell(s)
            else:
                next_cell = random.choice(to_visit)
                if next_cell == (left_col, j):
                    current_cell.has_left_wall = False
                    self._cells[left_col][j].has_right_wall = False
                if next_cell == (i, above_row):
                    current_cell.has_top_wall = False
                    self._cells[i][above_row].has_bottom_wall = False
                if next_cell == (right_col, j):
                    current_cell.has_right_wall = False
                    self._cells[right_col][j].has_left_wall = False
                if next_cell == (i, beneath_row):
                    current_cell.has_bottom_wall = False
                    self._cells[i][beneath_row].has_top_wall = False

                # recursively visit the next cell
                self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False




