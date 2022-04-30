import numpy as np
import scipy.constants as sp
import Animation
import math

class CelestialBodies:
    
    a = Animation.Animation(1400, 1000)
    scaling_factor_distance = 700/8e8 #700/6e9 # scaled / real
    bodies = []

    def __init__(self, mass=1, radius=0, velocity=(0,0,0), position=(0,0,0), name="System", color="red"):
        assert type(velocity) == tuple and len(velocity) == 3
        assert type(position) == tuple and len(position) == 3

        self.name = name
        self.mass = mass
        self.radius = radius
        self.velocity = tuple([v*self.scaling_factor_distance for v in velocity])
        self.position = tuple([s*self.scaling_factor_distance for s in position])
        self.delta_time = 1000
        self.display_size = math.floor(max(
            math.log(self.mass, self.a.display_log_base),
            self.a.min_display_size,
        ))
        self.color = color

        print("Mass for ", name, ": ",self.mass)
        print("Position for ", name, ": ",self.position)
        print("Velocity for ", name, ": ",self.velocity)
        print("Radius for ", name, ": ",self.radius)
        print("Display size for ", name, ": ",self.display_size)
        print()

    @property
    def total_force(self) -> tuple:
        '''Calculate the total force on self as all other objects in the system act on it (ie. planet1 and planet2 act on the sun)'''

        total = [0, 0, 0]
        for body in self.bodies:
            if (body is not self) and (issubclass(type(body), CelestialBodies)):
                f = self.force_on(body)
                total = [t + f for t,f in zip(total, f)]

        return tuple(total)

    def force_on(self, other) -> tuple:
        '''Calculate the force on self from other. Return a three dimentional tuple representing a force vector'''

        assert issubclass(type(other), CelestialBodies)

        other_pos = other.position
        force_list = [sp.G * self.mass * other.mass / (self.distance(other)**2)] * 3

        force_list = [force_list[i] * (other_pos[i]-self.position[i]) for i in range(3)]    
        return tuple(force_list)

    def distance(self, other):
        deltas = [((s-o)/self.scaling_factor_distance)**2 for s, o in zip(self.position, other.position)]

        return np.sqrt(np.sum(deltas))

    def draw(self):
        self.a.draw(self.bodies)

    def __str__(self) -> str:
        return self.name

    def update_position(self):
        
        self.update_velocity() 
        position_list =  [v * self.delta_time + p for v,p in zip(self.velocity, self.position)]
        self.position = tuple(position_list)

    def update_velocity(self):
        
        acceleration_list = [(f/self.mass)*(self.scaling_factor_distance**2) for f in self.total_force]
        self.acceleration = tuple(acceleration_list)

        velocity_list =  [a * self.delta_time + v for a,v in zip(acceleration_list, self.velocity)]
        self.velocity = tuple(velocity_list)
        
    def update_image(self):
        self.a.update(self.bodies)

    def update(self):
        self.update_position()

    def collect_data(self):
        pass


#the way the force funciton is defined isn't acceleration just a magnitude?
#I just don't see how we specify direction
# the acceleration is in the form of a vector so there is already a direction associated with that
#AH i didn't understand w the way total force was defined. gotcha
# either way, it works, look at the terminal
#EEEEEEEEEEEE
#is she animating

## Sun Class: Child of CelestialBodies Class
class Sun(CelestialBodies):

    orbiting_bodies = []

    def __init__(self, mass=0, radius=0, velocity=(0,0,0), position=(0,0,0), name="Sun", color="yellow"):
        self.name = name
        
        super().__init__(mass, radius, velocity, position, name, color)
        super().bodies.append(self)

    def __str__(self) -> str:
        return self.name

## Planet Class: Child of CelestialBodies Class
class Planet(CelestialBodies):

    def __init__(self, mass=0, radius=0, velocity=(0,0,0), position=(0,0,0), sun=None, name="Planet", color="blue"):
        self.name = name
        
        super().__init__(mass, radius, velocity, position, name, color)
        
        if sun is not None:
            self.sun = sun
            self.sun.orbiting_bodies.append(self)

        super().bodies.append(self)

    def __str__(self) -> str:
        return self.name

## Asteroid Class: Child of CelestialBodies Class
class Asteroids(CelestialBodies):

    def __init__(self, mass=0, radius=0, velocity=(0,0,0), position=(0,0,0), name="Asteroid", color="green"):
        self.name = name

        super().__init__(mass, radius, velocity, position, name, color)
        super().bodies.append(self)

    def __str__(self) -> str:
        return self.name

## Comet Class: Child of CelestialBodies Class
class Comet(CelestialBodies):
    
    def __init__(self, mass = 0, radius = 0, velocity = (0,0,0), position = (0,0,0), name = "Comet", color="sky blue"):
        self.name = name
        
        super().__init__(mass, radius, velocity, position, name, color)
        super().bodies.append(self)

    def change_mass(self):
        self.mass -= self.delta_mass

    def update(self):
        self.change_mass()
        self.update_position()

    @property
    def delta_mass(self):
        mass_change = 0.1 * self.delta_time #possibly also 0.37
        return mass_change
