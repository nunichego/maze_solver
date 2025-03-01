import time
import random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, 
                 cell_size_x, cell_size_y, win=None, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y  = cell_size_y
        self.__win = win
        self._cells = []
        self._seed = seed

        if self._seed != None and isinstance(self._seed, int):
            random.seed(self._seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

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

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            to_visit_directions = []
            if i - 1 >= 0 and self._cells[i - 1][j].visited != True:
                to_visit.append(self._cells[i - 1][j]) # left
                to_visit_directions.append('left')
            if i + 1 <= (self.__num_cols - 1) and self._cells[i + 1][j].visited != True:
                to_visit.append(self._cells[i + 1][j]) # right
                to_visit_directions.append('right')
            if j - 1 >= 0 and self._cells[i][j - 1].visited != True:
                to_visit.append(self._cells[i][j - 1]) # top
                to_visit_directions.append('top')
            if j + 1 <= (self.__num_rows - 1) and self._cells[i][j + 1].visited != True:
                to_visit.append(self._cells[i][j + 1]) # bottom
                to_visit_directions.append('bottom')

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            index = random.randrange(0, len(to_visit))
            chosen_cell = to_visit[index]
            if to_visit_directions[index] == 'left':
                chosen_cell.right_wall = False
                current_cell.left_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i - 1, j)
                self._break_walls_r(i - 1, j)
            elif to_visit_directions[index] == 'right':
                current_cell.right_wall = False
                chosen_cell.left_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i + 1, j)
                self._break_walls_r(i + 1, j)
            elif to_visit_directions[index] == 'top':
                current_cell.top_wall = False
                chosen_cell.bottom_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i, j - 1)
                self._break_walls_r(i, j - 1)
            else:
                current_cell.bottom_wall = False
                chosen_cell.top_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i, j + 1)
                self._break_walls_r(i, j + 1)




            
            

