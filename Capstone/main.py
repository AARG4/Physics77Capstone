import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import CelestialBodies as cb


if __name__ == "__main__":

    #system = cb.CelestialBodies()
    s = cb.Sun(mass=1230000000, radius=100)
    p = cb.Planet(mass=10, radius=20, position=(10,10,10))
    p2 = cb.Planet(mass=23, radius=50, position=(15,-1,-19))

    