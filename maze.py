import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, 
                 cell_size_x, cell_size_y, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y  = cell_size_y
        self.__win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self._cells.append(col_cells)
        for j in range(self.__num_rows):
            for i in range(self.__num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i , j):
        if self.__win is None:
            return
        x1 = self.__x1 + (i * self.__cell_size_x)
        x2 = self.__x1 + (i * self.__cell_size_x) + self.__cell_size_x
        y1 = self.__y1 + (j * self.__cell_size_y)
        y2 = self.__y1 + (j * self.__cell_size_y) + self.__cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.__num_cols - 1][self.__num_rows - 1].bottom_wall = False
        self._draw_cell(self.__num_cols - 1, self.__num_rows - 1)