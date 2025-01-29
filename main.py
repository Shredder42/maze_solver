from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10,10), Point(20,20)), 'blue')
    win.draw_line(Line(Point(100,50), Point(200,125)), 'red')
    win.draw_line(Line(Point(50,100), Point(125,200)))
    win.wait_for_close()


if __name__ == '__main__':
    main()