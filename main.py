import numpy as np
import matplotlib.pyplot as plt
import CelestialBodies as cb


if __name__ == "__main__":
    
    print("Hewo world")

#    system = cb.CelestialBodies()
    s = cb.Sun(mass=1230000000, radius=100)
    p = cb.Planet(mass=10, radius=20, position=(10,10,10))
    p2 = cb.Planet(mass=23, radius=50, position=(15,-1,-19))

    s.draw()
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
    
