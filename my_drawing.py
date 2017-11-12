from shapes import Triangle, Rectangle, Oval

rect1 = Rectangle()
rect1.set_width(50)
rect1.set_height(150)
rect1.set_color("yellow")
rect1.set_x(100)
rect1.set_y(100)

rect1.draw()

oval1 = Oval()

oval1.randomise(10, 100)
oval1.draw()
