class Window:
    def __init__(self, width, height):
        pass
    def draw_line(self, line, fill_color="black"):
        pass
    def redraw(self):
        pass
    def wait_for_close(self):
        pass
    def close(self):
        pass

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
