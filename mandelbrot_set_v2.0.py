# Create Mandelbrot Zoom using Turtle
import turtle
import mdb_draw

turtle.tracer(0,0)
pencil = turtle.Turtle()
pencil.hideturtle()
pencil.penup()
pencil.pensize(3)
pencil.color('gray')

class Cursor(object):
    def __init__(self, x_coor = 0, y_coor = 0, show = 0, side = 100, 
                 comp_num = -0.5+0j, size = 1.25, cycle = 1):
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.show = show
        self.side = side
        self.comp_num = comp_num
        self.size = size
        self.cycle = cycle

    def draw(self):
        pencil.clear()
        pencil.goto(self.x_coor - self.side, self.y_coor - self.side)
        pencil.pendown()

        for _ in range(4):
            pencil.forward(2 * self.side)
            pencil.left(90)

        pencil.penup()
        turtle.update()

    def appear(self):
        if self.show:
            self.show = 0
            pencil.clear()
            turtle.update()
        else:
            self.show = 1
            self.draw()

    def go_rt(self):
        if self.show: 
            self.x_coor += 10
            self.draw()

    def go_up(self):
        if self.show: 
            self.y_coor += 10
            self.draw()

    def go_lt(self):
        if self.show: 
            self.x_coor -= 10
            self.draw()

    def go_dn(self):
        if self.show: 
            self.y_coor -= 10
            self.draw()

    def jump_rt(self):
        if self.show: 
            self.x_coor += 50
            self.draw()

    def jump_up(self):
        if self.show: 
            self.y_coor += 50
            self.draw()

    def jump_lt(self):
        if self.show: 
            self.x_coor -= 50
            self.draw()

    def jump_dn(self):
        if self.show: 
            self.y_coor -= 50
            self.draw()

    def get_large(self):
        if self.show and self.side < 450: self.side += 10
        self.draw()

    def get_small(self):
        if self.show and self.side > 10: self.side -= 10
        self.draw()

    def zoom_in(self):
        self.comp_num += complex((self.x_coor/720) * self.size * 1.6,
                                 (self.y_coor/450) * self.size)
        self.size *= (self.side/450)
        mdb_draw.mplot(self.comp_num, self.size, self.cycle)

    def restart(self):
        self.comp_num = -0.5+0j
        self.size = 1.25
        self.cycle = 1
        mdb_draw.mplot(self.comp_num, self.size, self.cycle)

    def magnify(self):
        self.cycle += 1
        mdb_draw.mplot(self.comp_num, self.size, self.cycle)

    def diminish(self):
        self.cycle -= 1
        mdb_draw.mplot(self.comp_num, self.size, self.cycle)

if __name__ == '__main__':
    mdb_draw.mplot(-0.5+0j, 1.25, 1)
    # mdb_draw.jplot(0+0j, -1+0j, 2, 1)
    cursor = Cursor()

    turtle.listen()

    turtle.onkeypress(cursor.go_rt, 'd')
    turtle.onkeypress(cursor.go_up, 'w')
    turtle.onkeypress(cursor.go_lt, 'a')
    turtle.onkeypress(cursor.go_dn, 's')

    turtle.onkeypress(cursor.jump_rt, 'h')
    turtle.onkeypress(cursor.jump_up, 't')
    turtle.onkeypress(cursor.jump_lt, 'f')
    turtle.onkeypress(cursor.jump_dn, 'g')

    turtle.onkeypress(cursor.appear, 'j')
    turtle.onkeypress(cursor.get_large, 'k')
    turtle.onkeypress(cursor.get_small, 'l')

    turtle.onkeypress(cursor.zoom_in, 'u')
    turtle.onkeypress(cursor.restart, 'i')
    turtle.onkeypress(cursor.magnify, 'o')
    turtle.onkeypress(cursor.diminish, 'p')

    turtle.mainloop()
