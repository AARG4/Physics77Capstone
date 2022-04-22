import turtle

class Animation(turtle.Turtle):

    min_display_size = 20
    display_log_base = 1.1

    def __init__(self, width, height):
        super().__init__()

        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor("black")
        

    def draw(self, bodies):
        for body in bodies:
            self.setx(10*body.position[0])
            self.sety(10*body.position[1])
            self.pendown()
            self.dot(body.display_size, body.color)
            self.penup()


    def update(self, bodies):
        for body in bodies:
            body.update_position()
        
        self.clear()

        self.draw(bodies)
        self.solar_system.update()
        
        

