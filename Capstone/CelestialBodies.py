import numpy as np
import scipy.constants as sp

class CelestialBodies:
    
    all_bodies = []

    def __init__(self, mass=0, radius=0, velocity=(0,0,0), position=(0,0,0), name="System"):
        assert type(velocity) == tuple and len(velocity) == 3
        assert type(position) == tuple and len(position) == 3

        self.name = name
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.position = position

    @property
    def total_force(self) -> tuple:
        '''Calculate the total force on self as all other objects in the system act on it (ie. planet1 and planet2 act on the sun)'''

        total = [0, 0, 0]
        for body in self.all_bodies:
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
        deltas = [(s-o)**2 for s, o in zip(self.position, other.position)]

        return np.sqrt(np.sum(deltas))


    def __str__(self) -> str:
        return self.name



## Sun Class: Child of CelestialBodies Class
class Sun(CelestialBodies):

    orbiting_bodies = []

    def __init__(self, mass=0, radius=0, velocity=(0,0,0), position=(0,0,0), name="Sun"):
        self.name = name
        
        super().__init__(mass, radius, velocity, position)
        super().all_bodies.append(self)

    def __str__(self) -> str:
        return self.name



## Planet Class: Child of CelestialBodies Class
class Planet(CelestialBodies):

    def __init__(self, mass=0, radius=0, velocity=(0,0,0), position=(0,0,0), sun=None, name="Planet"):
        self.name = name
        
        super().__init__(mass, radius, velocity, position)
        
        if sun is not None:
            self.sun = sun
            self.sun.orbiting_bodies.append(self)

        super().all_bodies.append(self)

    def __str__(self) -> str:
        return self.name



## Asteroid Class: Child of CelestialBodies Class
class Asteroids(CelestialBodies):

    def __init__(self, mass=0, radius=0, velocity=(0,0,0), position=(0,0,0), name="Asteroid"):
        self.name = name

        super().__init__(mass, radius, velocity, position, name)
        super().all_bodies.append(self)

    def __str__(self) -> str:
        return self.name

