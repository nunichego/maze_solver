from graphics import Window, Line, Point

def main():

    win = Window(800, 600)

    line_1 = Line(Point(200, 200), Point(400, 400))
    line_2 = Line(Point(600, 200), Point(700, 400))
    lines = [line_1, line_2]
    for line in lines:
        win.draw_line(line)
    win.wait_for_close()

if __name__ == "__main__":
    main()