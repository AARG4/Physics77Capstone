import numpy as np
import scipy.constants as sp
import Animation
import math
import csv

class CelestialBodies:
    
    a = Animation.Animation(1400, 1000)
    m_per_km = 1000 #km -> m
    scaling_factor_distance = 700/5e9 #scaled / real # Allows for vision of everything from sun to just part neptune
    scaling_factor_velocity =  1 # keeps velocity in units km/s
    bodies = []
    delta_time = a.timestep

    def __init__(self, mass=.0000000001, radius=0, velocity=(0,0,0), position=(0,0,0), name="System", color="red"):
        assert type(velocity) == tuple and len(velocity) == 3
        assert type(position) == tuple and len(position) == 3

        self.name = name
        self.mass = mass
        self.radius = radius
        self.acceleration = (0, 0, 0)
        self.velocity = tuple(v*self.scaling_factor_velocity for v in velocity) # km/s
        
        # Position will be input in units of km, we will adjust accordingly when calculating distance
        self.position = position #km
        
        if not isinstance(self, Sun):
            self.display_size = math.floor(max(
                math.log(self.mass, self.a.display_log_base),
                self.a.min_display_size,
            ))
        else:
            self.display_size = 50
        
        self.color = color

        self.print_attributes()

        self.initialize_writer()

    
    @property
    def total_force(self) -> tuple:
        '''Calculate the total force on self as all other objects in the system act on it (ie. planet1 and planet2 act on the sun)'''

        #print("\nCalculating total force")
        total = [0, 0, 0]
        for body in self.bodies:
            if (body is not self) and (issubclass(type(body),\
                CelestialBodies)):
                force = self.force_on(body)
                total = [t + f for t,f in zip(total, force)]
        #print("Acc.", self.name ,"Magnitude", np.sqrt(total[0]**2 + total[1]**2 + total[2]**2))
        return tuple(total)

    def force_on(self, other) -> tuple:
        '''Calculate the force on self from other. Return a three dimensional tuple representing a force vector'''

        assert issubclass(type(other), CelestialBodies)
        # F = G * m1 * m2 / (r**2)

        distance, dist_vec_unit = self.distance_to(other)
        force = (sp.G * self.mass * other.mass) / ((self.m_per_km*distance)**2) 
        force_list = [-d * force for d in dist_vec_unit]
        
        return tuple(force_list)

    def distance_to(self, other):
        '''Calculates the distance between self and other and returns the magnitude and unit vector for the position
        of one with respect to the other. Other will be some subclass of CelestialBodies'''

        assert issubclass(type(other), CelestialBodies)

        dist_list = [((s - o)/1e4)**2 for s,o in zip(self.position, other.position)] #squared distances
        dist = np.sqrt(np.sum(dist_list)) * 1e4 #distance magnitude # the 10000 is used to allow python to actually do the calculation because some numbers are too big to take the sqrt of
        dist_vector_unit = [(s-o)/dist for s,o in zip(self.position, other.position)] 
        
        return dist, dist_vector_unit

    def draw(self):
        '''Calls draw function an Animator to draw self'''

        self.a.draw(self.bodies)

    def update_position(self):
        '''Updates position vector of celestial body, calls update_velocity'''

        self.update_velocity() 
        position_list =  [v * self.delta_time + p for v,p in zip(self.velocity, self.position)]
        self.position = tuple(position_list)
        # print("Pos", self.name, self.position)

    def update_velocity(self):
        '''Updates velocity vector of self, calls update_acceleration'''

        self.update_acceleration()
        velocity_list =  [(a * self.delta_time) + v for a,v in zip(self.acceleration, self.velocity)]
        self.velocity = tuple(velocity_list)
        # print("Vel",self.name, self.velocity)

    def update_acceleration(self):
        '''Uses total_force to calcuate acceleration vector of self'''
        accleration_list = [(f/self.mass)/self.m_per_km for f in self.total_force]
        self.acceleration = tuple(accleration_list)
        # print("Acc",self.name, self.acceleration)

    def update_image(self):
        self.a.update(self.bodies)

    def update(self):
        '''Updates various attributes of the Celestial Body'''
        self.update_position()
        # self.collect_data()

    def initialize_writer(self):
        '''initialize csv file here'''

        self.datafile = open(f"Simulation_CSVfiles_Comet/{self.name}.csv", "w")
        init_writer = csv.writer( self.datafile, delimiter = ',', quotechar = '', quoting = csv.QUOTE_NONE )
        init_writer.writerow(["Mass", "Time", "X", "Y", "Z", "Xvel", "YVel", "ZVel", "XAc", "YAc", "ZAc"])
        init_writer.writerow([self.mass, self.a.date, self.position[0], self.position[1], self.position[2], self.velocity[0], self.velocity[1], self.velocity[2], self.acceleration[0], self.acceleration[1], self.acceleration[2]])

    def collect_data(self):
        '''Writes data to a csv file, this info includes: name, position, velocity and other information'''
        planetwriter = csv.writer(self.datafile, delimiter = ",", quotechar = '', quoting = csv.QUOTE_NONE )
        planetwriter.writerow([self.mass, self.a.date, self.position[0], self.position[1], self.position[2], self.velocity[0], self.velocity[1], self.velocity[2], self.acceleration[0], self.acceleration[1], self.acceleration[2]])

    def close_csvs(self):
        for body in self.bodies:
            body.datafile.close()

    def end_cond(self) -> bool:
        return self.a.end_sim()

    def print_attributes(self):
        '''Prints out various attributes of Celestial Body'''

        print("Mass for ", self.name, ": ",self.mass)
        print("Position for ", self.name, ": ",self.position)
        print("Velocity for ", self.name, ": ",self.velocity)
        print("Acceleration for ", self.name, ": ", self.acceleration)
        print("Radius for ", self.name, ": ",self.radius)
        print("Display size for ", self.name, ": ",self.display_size)
        print()
 
    def __str__(self) -> str:
        return self.name

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

    def update_mass(self):
        self.mass -= self.delta_mass

    def update(self):
        self.update_mass()
        self.update_position()
        # self.collect_data()

    @property
    def delta_mass(self):
        mass_change = 1.0 * self.delta_time #possibly also 0.37
        return mass_change
