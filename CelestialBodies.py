import numpy as np
import scipy.constants as sp
import Animation
import math

class CelestialBodies:
    
    a = Animation.Animation(1000, 1000)
    bodies = []

    def __init__(self, mass=1, radius=0, velocity=(0,0,0), position=(0,0,0), name="System", color="red"):
        assert type(velocity) == tuple and len(velocity) == 3
        assert type(position) == tuple and len(position) == 3

        self.name = name
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.position = position
        self.display_size = max(
            math.log(self.mass, self.a.display_log_base),
            self.a.min_display_size,
        )
        self.color = color

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
        deltas = [(s-o)**2 for s, o in zip(self.position, other.position)]

        return np.sqrt(np.sum(deltas))

    def draw(self):
        self.a.draw(self.bodies)

    def __str__(self) -> str:
        return self.name

    def OrbitEquation(w, t, m1, m2): # w is an array containing positions and velocities
        r1 = w[:2]
        v1 = w[2:4]
        
        r12 = np.linalg.norm(r1)
        
        dv1bydt = m2*(-r1)/r12**3  # derivative of velocity

        dr1bydt = v1 # derivative of position 
        
        r_derivs = dr1bydt
        v_derivs = dv1bydt
        derivs = np.concatenate((r_derivs, v_derivs)) # joining the two arrays
        
        return derivs




## Sun Class: Child of CelestialBodies Class
class Sun(CelestialBodies):

    orbiting_bodies = []

    def __init__(self, mass=0, radius=0, velocity=(0,0,0), position=(0,0,0), name="Sun", color="yellow"):
        self.name = name
        
        super().__init__(mass, radius, velocity, position, name, color)
        super().bodies.append(self)

        print(self.color)

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

class Comet(CelestialBodies):
    
    def __init__(self,ice_content = 0, mass = 0, radius = 0, velocity = (0,0,0), position = (0,0,0), name = "Comet", color="sky blue"):
        self.name = name
        self.ice_content = ice_content

        super().__init__(mass, radius, velocity, position, name, color)
        super().bodies.append(self)

    def change_mass(self):
        self.mass -= self.delta_mass

    @property
    def delta_mass(self):
        pass
