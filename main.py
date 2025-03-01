from graphics import Window
from cell import Cell

def main():

    win = Window(800, 600)

    c = Cell(win)
    c.left_wall = False
    c.draw(50, 50, 100, 100)

    y = Cell(win)
    y.right_wall = False
    y.draw(125, 125, 200, 200)

    b = Cell(win)
    b.bottom_wall = False
    b.draw(225, 225, 250, 250)

    d = Cell(win)
    d.top_wall = False
    d.draw(300, 300, 500, 500)

    b.draw_move(d, True)
    c.draw_move(y, False)



    win.wait_for_close()

if __name__ == "__main__":
    main()