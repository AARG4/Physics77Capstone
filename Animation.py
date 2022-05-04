# Inspiration and starting code for Animation module was taken from:
# https://thepythoncodingbook.com/2021/09/29/simulating-orbiting-planets-in-a-solar-system-using-python-orbiting-planets-series-1/

import turtle

class Animation(turtle.Turtle):

    min_display_size = 20
    display_log_base = 12

    def __init__(self, width, height):
        super().__init__()

        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor("black")
        self.hideturtle()
        

    def draw(self, bodies):
        for body in bodies:
            self.setx(body.position[0]*body.scaling_factor_distance)
            self.sety(body.position[1]*body.scaling_factor_distance)
            self.pendown()
            self.dot(body.display_size, body.color)
            self.penup()


    def update(self, bodies):
        for body in bodies:
            body.update()
        
        self.clear()

        self.draw(bodies)
        self.solar_system.update()
        
        

