import numpy as np
import matplotlib.pyplot as plt
import CelestialBodies as cb
import time

if __name__ == "__main__":
    
    print("Hewo world")

    system = cb.CelestialBodies()
    #s = cb.Sun(mass=1000, radius=100000)
    s = cb.Sun(mass=1.9891e30, radius=696000, name="Sun")
    earth = cb.Planet(mass=5.972e24, radius=6378, position=(149598262,0,0), velocity=(0,29.78, 0), color="Blue", name="Earth")
    jupiter = cb.Planet(mass=18.98e26, radius=71492, position=(778340821,0,0), velocity=(0,13.1,0), color="Green", name="Jupiter")
    #pluto = cb.Planet(mass=1.2e22, radius=1185, position=(5.91e9,0,0), velocity=(0,4.72,0), color="Red", name="Pluto")
    #p2 = cb.Planet(mass=23, radius=200, position=(15,-1,-19), name="Pluto")
    #a1 = cb.Asteroids(mass=1, radius=2, position=(-15,7,0))
    #c1 = cb.Comet(mass=2, radius=4, position=(0,-30, 0), velocity=(-.25, 0, 0))

    system.draw()

    #while True:
    for _ in range(10):
        #system.collect_data()
        system.update_image()
        time.sleep(.05)

'''
    init_params = np.array([r1, v1])
    init_params = init_params.flatten()
    time_span = np.linspace(0, 5, 500)

    sol = scipy.integrate.odeint(OrbitEquation, init_params, time_span, args=(massExoplanet,massStar))

    r1_sol = sol[:,:2]

    metadata = dict(title='Exoplanet orbit', artist='Matplotlib')
    writer = FFMpegWriter(fps=50, metadata=metadata, bitrate=200000) # change fps for different frame rates
    fig = plt.figure(dpi=200) 

    metadata = dict(title='Exoplanet orbit', artist='Matplotlib')
    writer = FFMpegWriter(fps=50, metadata=metadata, bitrate=200000) # change fps for different frame rates
    fig = plt.figure(dpi=200)   
    fig, ax = plt.subplots()

    with writer.saving(fig, "orbit.mp4", dpi=200):
        for i in range(len(time_span)):

            ax.clear()

            ax.plot(r1_sol[:i,0],r1_sol[:i,1],color="blue", alpha=0.5)
            ax.scatter(r1_sol[i,0],r1_sol[i,1],color="blue",marker="o",s=500, zorder=5) # planet

            yP = r1_sol[i,1]
            if (yP >= -rStar - rPlanet and yP <= rStar + rPlanet):
            
            ax.scatter(0, 0, color="orange",s=3000, zorder=5) # star
            
            ax.set_xlim(-1.5, 1.5)
            ax.set_ylim(-1.5, 1.5)
            
            plt.draw()
            plt.pause(0.01)
            writer.grab_frame()
'''
    



## Planet Data:
#https://www.britannica.com/place/Pluto-dwarf-planet