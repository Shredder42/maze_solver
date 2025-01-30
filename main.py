from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    # win.draw_line(Line(Point(10,10), Point(20,20)), 'blue')
    # win.draw_line(Line(Point(100,50), Point(200,125)), 'red')
    # win.draw_line(Line(Point(50,100), Point(125,200)))
    # win.draw_cell(Cell(200, 200, 300, 300))
    # win.draw_cell(Cell(400, 400, 500, 500, has_left_wall=True, has_right_wall=False, has_top_wall=False))
    # cell1 = Cell(win)
    # cell1.draw(400, 400, 500, 500)
    # cell2 = Cell(win)
    # cell2.draw(500, 400, 600, 500)
    # cell1.draw_move(cell2, undo=True)
    maze = Maze(0,0,30,40,20,20,win)
    win.wait_for_close()


if __name__ == '__main__':
    main()