from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win

    def draw(self, x1, y1, x2, y2):

        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line, "white")

        if self.right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, "white")

        if self.top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line)
        else:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line, "white")

        if self.bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        center_from = Point((self.__x2 - self.__x1) / 2 + 
                            self.__x1, (self.__y2 - self.__y1) / 2 + self.__y1)
        center_to = Point((to_cell.__x2 - to_cell.__x1) / 2 + 
                          to_cell.__x1, (to_cell.__y2 - to_cell.__y1) / 2 + to_cell.__y1)
        line = Line(center_from, center_to, )
        if undo == False:
            self.__win.draw_line(line, "red")
        else:self.__win.draw_line(line, "gray")