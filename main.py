import CelestialBodies as cb
import time

if __name__ == "__main__":
    
    print("Hewo solar system!")

    system = cb.CelestialBodies()

    sun = cb.Sun(mass=1.9891e30, radius=695700, name="Sun")

    # Inner planets
    mercury = cb.Planet(mass=3.3020e23, radius=2440, position=(-54588657,-35074887,2141881), velocity=(16.32924805980451,-38.83572705086910,-4.671423362502626), color="grey", name="Mercury")
    venus = cb.Planet(mass=48.685e23, radius=6051.84, position=(-91833808,55566712,6061609), velocity=(-18.27476334169853,-30.13420372604397,0.6412158166426387), color="orange", name="Venus")
    earth = cb.Planet(mass=5.97219e24, radius=6371.01, position=(139687616,52489174,-2713.707975), velocity=(-10.95375967554877,27.78172565860283,-.002208848641529926), color="light blue", name="Earth")
    mars = cb.Planet(mass=6.4171e23, radius=3389.92, position=(-232221048,90134689,7587936), velocity=(-7.859033317296808,-20.51785238310983,-0.2370875083210473), color="red", name="Mars")

    # Outer planets
    jupiter = cb.Planet(mass=18.98e26, radius=71492, position=(-687972738,-435146345,17201259), velocity=(6.832,-10.434,-0.109), color="green", name="Jupiter")
    saturn = cb.Planet(mass=5.683e26, radius=60268, position=(-55467921,-1504099277,28350676), velocity=(9.130,-.394,-.356), color="beige", name="Saturn")
    uranus = cb.Planet(mass=8.861e25, radius=25559, position=(2672223048,1315575668,-29714767), velocity=(-3.049,5.782,0.0609), color="cyan", name="Uranus")
    neptune = cb.Planet(mass=1.024e26, radius=24622, position=(4279829088,-1321863342,-71417656), velocity=(1.575,5.217,-.143), color="blue", name="Neptune")
    
    #planet_nine = cb.Asteroids(mass=42e25, radius=0.1, velocity=(-30.84436302295012,-1.38938157570143,0), position=(2672223048,0,29714767),name="Planet 9", color="hot pink")


    oumuamua_asteroid = cb.Asteroids(mass=42e3, radius=0.1, velocity=(44.84436302295012,10.38938157570143,14.33792560371971), position=(144932593,73907368,-10693289),name="Oumuamua", color="hot pink")
    # oumuamua_comet = cb.Comet(mass=42e3, radius=0.1, velocity=(44.84436302295012,10.38938157570143,14.33792560371971), position=(144932593,73907368,-10693289),name="Oumuamua Comet", color="hot pink")    
    # pluto = cb.Planet(mass=1.2e22, radius=1185, position=(5.91e9,0,0), velocity=(0,4.72,0), color="Red", name="Pluto")
    
    system.draw()

    while True:
    #for _ in range(0):
        system.update_image()
        time.sleep(.01)
        
        
        if system.end_cond():
            #system.close_csvs()
            break
        

    print("Sim ended")


### Planet Data:
# oumuamua_jpl_dataset.txt