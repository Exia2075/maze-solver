import sys
import unittest

sys.modules['graphics'] = __import__('graphics_stub')

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_square(self):
        num_cols = 5
        num_rows = 5
        m2 = Maze(0, 0, num_rows, num_cols, 15, 15)
        self.assertEqual(len(m2._Maze__cells), num_cols)
        self.assertEqual(len(m2._Maze__cells[0]), num_rows)

    def test_maze_rectangular(self):
        num_cols = 7
        num_rows = 3
        m3 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m3._Maze__cells), num_cols)
        self.assertEqual(len(m3._Maze__cells[0]), num_rows)

    def test_maze_single_cell(self):
        num_cols = 1
        num_rows = 1
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m4._Maze__cells), num_cols)
        self.assertEqual(len(m4._Maze__cells[0]), num_rows)

    def test_maze_no_window(self):
        num_cols = 4
        num_rows = 4
        m5 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m5._Maze__cells), num_cols)
        self.assertEqual(len(m5._Maze__cells[0]), num_rows)
        self.assertIsNone(m5._Maze__win)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._Maze__cells[0][0].has_top_wall, False)
        self.assertEqual(m1._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall, False)

    def test_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(m._Maze__cells[i][j].visited)

    def test_solve_returns_true(self):
        m = Maze(0, 0, 5, 5, 10, 10)
        self.assertTrue(m.solve())

    def test_solve_single_cell(self):
        m = Maze(0, 0, 1, 1, 10, 10)
        self.assertTrue(m.solve())

    def test_solve_rectangular(self):
        m = Maze(0, 0, 3, 7, 10, 10)
        self.assertTrue(m.solve())

    def test_solve_marks_cells_visited(self):
        m = Maze(0, 0, 4, 4, 10, 10)
        m.solve()
        visited_count = 0
        for i in range(4):
            for j in range(4):
                if m._Maze__cells[i][j].visited:
                    visited_count += 1
        self.assertGreater(visited_count, 0)

    def test_solve_goal_cell_visited(self):
        cols = 5
        rows = 5
        m = Maze(0, 0, rows, cols, 10, 10)
        m.solve()
        self.assertTrue(m._Maze__cells[cols - 1][rows - 1].visited)

    def test_solve_with_seed(self):
        m = Maze(0, 0, 6, 6, 10, 10, seed=10)
        self.assertTrue(m.solve())

if __name__ == "__main__":
    unittest.main()