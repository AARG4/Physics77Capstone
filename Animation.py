import turtle

class Animation(turtle.Turtle):

    min_display_size = 20
    display_log_base = 1.1
    bodies = []

    def __init__(self, width, height):
        super().__init__()

        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor("black")
        

    def draw(self):
        print("Draw")
        for body in self.bodies:
            
            self.dot(body.display_size)

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)