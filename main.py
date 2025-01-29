from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    # win.draw_line(Line(Point(10,10), Point(20,20)), 'blue')
    # win.draw_line(Line(Point(100,50), Point(200,125)), 'red')
    # win.draw_line(Line(Point(50,100), Point(125,200)))
    # win.draw_cell(Cell(200, 200, 300, 300))
    # win.draw_cell(Cell(400, 400, 500, 500, has_left_wall=True, has_right_wall=False, has_top_wall=False))
    cell = Cell(win)
    cell.draw(400, 400, 500, 500)
    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(300, 300, 500, 500)
    win.wait_for_close()


if __name__ == '__main__':
    main()