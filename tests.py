import unittest
from unittest.mock import MagicMock, patch
from maze import Maze

class Tests(unittest.TestCase):
    def setUp(self):
        self.mock_win = MagicMock()

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_initialization(self):
        maze = Maze(10, 20, 5, 6, 30, 40, self.mock_win)
        
        self.assertEqual(maze._Maze__x1, 10)
        self.assertEqual(maze._Maze__y1, 20)
        self.assertEqual(maze._Maze__num_rows, 5)
        self.assertEqual(maze._Maze__num_cols, 6)
        self.assertEqual(maze._Maze__cell_size_x, 30)
        self.assertEqual(maze._Maze__cell_size_y, 40)
        self.assertEqual(maze._Maze__win, self.mock_win)

        self.assertEqual(len(maze._cells), 6)  # Number of columns
        for col in maze._cells:
            self.assertEqual(len(col), 5)  # Number of rows

    def test_create_cells(self):
        """Test that cells are created properly"""
        with patch('maze.Cell') as mock_cell:
            mock_cell_instance = MagicMock()
            mock_cell.return_value = mock_cell_instance
            
            maze = Maze(0, 0, 3, 2, 10, 10, self.mock_win)
            
            # Check correct number of Cell instances created
            self.assertEqual(mock_cell.call_count, 6)  # 2 cols * 3 rows
            
            # Check cells 2D array structure
            self.assertEqual(len(maze._cells), 2)
            self.assertEqual(len(maze._cells[0]), 3)
            self.assertEqual(len(maze._cells[1]), 3)

    def test_draw_cell(self):
        """Test that draw_cell properly calculates coordinates and calls cell.draw"""
        with patch('maze.Cell') as mock_cell:
            mock_cell_instance = MagicMock()
            mock_cell.return_value = mock_cell_instance
            
            maze = Maze(10, 20, 2, 2, 30, 40, self.mock_win)
            
            # Reset mock to clear initialization calls
            mock_cell_instance.draw.reset_mock()
            
            # Manually call _draw_cell to test it
            maze._draw_cell(0, 0)
            
            # Check if draw was called with correct coordinates
            mock_cell_instance.draw.assert_called_with(10, 20, 40, 60)
            
            # Test another cell
            mock_cell_instance.draw.reset_mock()
            maze._draw_cell(1, 1)
            mock_cell_instance.draw.assert_called_with(40, 60, 70, 100)
    
    def test_animate(self):
        """Test that animate calls window redraw"""
        maze = Maze(0, 0, 1, 1, 10, 10, self.mock_win)
        
        # Reset the mock to clear initialization calls
        self.mock_win.reset_mock()
        
        # Call animate
        with patch('time.sleep') as mock_sleep:
            maze._animate()
            
            # Verify window redraw was called
            self.mock_win.redraw.assert_called_once()
            
            # Verify sleep was called with correct duration
            mock_sleep.assert_called_once_with(0.01)
            
    def test_animate_no_window(self):
        """Test that animate does nothing when window is None"""
        maze = Maze(0, 0, 1, 1, 10, 10, None)
        
        # Should not raise exceptions
        with patch('time.sleep') as mock_sleep:
            maze._animate()
            
            # Sleep should not be called
            mock_sleep.assert_not_called()
    
    def test_break_entrance_and_exit(self):
        """Test that entrance and exit walls are properly removed"""
        with patch('maze.Cell') as mock_cell:
            # Create mock cells with properties we can check
            cells = []
            for i in range(4):  # We'll create a 2x2 maze, so 4 cells
                mock_instance = MagicMock()
                mock_instance.top_wall = True
                mock_instance.bottom_wall = True
                cells.append(mock_instance)
            
            # Return a different mock cell for each call
            mock_cell.side_effect = cells
            
            # Create a 2x2 maze
            maze = Maze(0, 0, 2, 2, 10, 10, None)
            
            # Verify entrance (top-left cell) has top wall removed
            self.assertFalse(maze._cells[0][0].top_wall)
            
            # Verify exit (bottom-right cell) has bottom wall removed
            self.assertFalse(maze._cells[1][1].bottom_wall)
    
    def test_draw_cell_no_window(self):
        """Test that _draw_cell does nothing when window is None"""
        maze = Maze(0, 0, 1, 1, 10, 10, None)
        
        # Create a mock cell to replace the real one
        mock_cell = MagicMock()
        maze._cells[0][0] = mock_cell
        
        # Call _draw_cell
        maze._draw_cell(0, 0)
        
        # Verify draw was not called
        mock_cell.draw.assert_not_called()

    

if __name__ == "__main__":
    unittest.main()