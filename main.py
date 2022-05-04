import numpy as np
import matplotlib.pyplot as plt
import CelestialBodies as cb
import time

if __name__ == "__main__":
    
    print("Hewo solar system!")

    system = cb.CelestialBodies()

    sun = cb.Sun(mass=1.9891e30, radius=696000, name="Sun")

    # Inner planets
    mercury = cb.Planet(mass=3.3010e23, radius=2440, position=(58e6,0,0), velocity=(0,47.36,0), color="grey", name="Mercury")
    venus = cb.Planet(mass=4.87e24, radius=6051, position=(108209475,0,0), velocity=(0,35,0), color="orange", name="Venus")
    earth = cb.Planet(mass=5.972e24, radius=6378, position=(149598262,0,0), velocity=(0,29.78,0), color="light blue", name="Earth")
    mars = cb.Planet(mass=6.417e23, radius=3396, position=(227943824,0,0), velocity=(0,24.1,0), color="red", name="Mars")

    # Outer planets
    jupiter = cb.Planet(mass=18.98e26, radius=71492, position=(778340821,0,0), velocity=(0,13.1,0), color="green", name="Jupiter")
    saturn = cb.Planet(mass=5.683e26, radius=60268, position=(1426666000,0,0), velocity=(0,9.6 ,0), color="beige", name="Saturn")
    uranus = cb.Planet(mass=8.861e25, radius=25559, position=(2870658000,0,0), velocity=(0,6.8,0), color="cyan", name="Uranus")
    neptune = cb.Planet(mass=1.024e26, radius=24622, position=(4498250000,0,0), velocity=(0,5.43,0), color="blue", name="Neptune")

    #pluto = cb.Planet(mass=1.2e22, radius=1185, position=(5.91e9,0,0), velocity=(0,4.72,0), color="Red", name="Pluto")
    
    system.draw()

    while True:
    #for _ in range(365):
        #system.collect_data()
        system.update_image()
        time.sleep(.01)

    
### Planet Data:

## Mercury
# https://www.britannica.com/place/Mercury-planet/Basic-astronomical-data
# https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html

## Venus
# https://www.britannica.com/place/Venus-planet#ref54177

## Earth
# https://www.britannica.com/place/Earth/Basic-planetary-data

## Mars
# https://www.britannica.com/place/Mars-planet

## Jupiter

## Saturn
# https://www.britannica.com/place/Saturn-planet#ref54278

## Uranus

## Neptune
# https://www.britannica.com/place/Neptune-planet/Basic-astronomical-data
# https://nssdc.gsfc.nasa.gov/planetary/factsheet/neptunefact.html

## Pluto
# https://www.britannica.com/place/Pluto-dwarf-planet