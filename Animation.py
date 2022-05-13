# Inspiration and starting code for Animation module was taken from:
# https://thepythoncodingbook.com/2021/09/29/simulating-orbiting-planets-in-a-solar-system-using-python-orbiting-planets-series-1/

import turtle
import datetime
import CelestialBodies as cb
import numpy as np
import math

class Animation(turtle.Turtle):

    min_display_size = 20
    display_log_base = 15
    base = 1.02

    timestep = 86400 # seconds in an hour so the simulation updates on one earth day intervals
    
    date = datetime.datetime(2017, 10, 14, 00, 00, 00)
    delta_time = datetime.timedelta(seconds=timestep)

    def __init__(self, width, height):
        super().__init__()

        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor("black")
        self.hideturtle()
        

    def draw(self, bodies):

        # Writing Time on Screen
        self.setx(-660)
        self.sety(320)
        self.pendown()
        self.color("white")
        self.write(self.date, move=False, font=('arial',40,'bold'),align='left') 
        self.penup()

        # Drawing Bodies
        for body in bodies:
            self.setx(body.position[0]*body.scaling_factor_distance)
            self.sety(body.position[1]*body.scaling_factor_distance)
            self.pendown()
            self.dot(body.display_size, body.color)

            if body.name not in ["Mercury", "Venus", "Earth", "Mars"]:
                self.setx((body.display_size+body.position[0])*body.scaling_factor_distance)
                self.sety((body.display_size+body.position[1])*body.scaling_factor_distance)
                self.write(body.name, move=False, font=('arial',20,'bold'),align='left')
                
            self.penup()
            
            '''
            if not isinstance(body, cb.Sun):
                if body.position[0] < 0:
                    self.setx(-math.log(np.abs(body.position[0]*body.scaling_factor_distance), self.base))
                else:
                    self.setx(math.log(body.position[0]*body.scaling_factor_distance, self.base))
                
                
                if body.position[1] < 0:
                    self.sety(-math.log(np.abs(body.position[1]*body.scaling_factor_distance), self.base))
                else:
                    self.sety(math.log(body.position[1]*body.scaling_factor_distance, self.base))
                
                self.pendown()
                self.dot(body.display_size, body.color)
                self.penup()
            else:
                self.setx(body.position[0]*body.scaling_factor_distance)
                self.sety(body.position[1]*body.scaling_factor_distance)
                self.pendown()
                self.dot(body.display_size, body.color)
                self.penup()
            '''


    def update(self, bodies):
        self.date = self.date + self.delta_time

        for body in bodies:
            body.update()

        self.clear()

        self.draw(bodies)
        self.solar_system.update()


    def end_sim(self):
        return self.date == datetime.datetime(2018, 1, 2, 00, 00, 00)
            

