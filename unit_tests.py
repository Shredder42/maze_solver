import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_2(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_3(self):
        num_cols = 3
        num_rows = 7
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_entrance_and_exit_broken(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_cols-1][num_rows-1].has_bottom_wall, False)
        # self.assertEqual(m1._cells[num_cols-1][num_rows-1].has_top_wall, True)

    # these are no longer neccessarily true
    # def test_other_walls_intact(self):
    #     num_cols = 5
    #     num_rows = 5
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(m1._cells[2][3].has_top_wall, True)
    #     self.assertEqual(m1._cells[2][3].has_bottom_wall, True)

    def test_visited_property(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(cell.visited, False)


if __name__ == '__main__':
    unittest.main()