import Data_Storage as ds
import matplotlib.pyplot as plt
import numpy as np


def pos_percentage_diff(x_real,y_real,z_real,x_exp,y_exp,z_exp):
    r = np.sqrt(x_real**2 + y_real**2 + z_real**2)
    r1 = np.sqrt(x_exp**2 + y_exp**2 + z_exp**2)
    diff = r-r1
    perc = diff/r 
    return np.abs(perc*100)

def radial_dist(x,y,z):
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    return np.sqrt(x**2 + y**2 + z**2)

mer_err = []
for i in range(len(ds.me_re_xcord)):
    percdif = pos_percentage_diff(ds.me_re_xcord[i], ds.me_re_ycord[i], ds.me_re_zcord[i], ds.me_sim_xcord[i], ds.me_sim_ycord[i], ds.me_sim_zcord[i])
    mer_err.append(percdif)

vn_err = []
for i in range(len(ds.vn_re_xcord)):
    percdif = pos_percentage_diff(ds.vn_re_xcord[i], ds.vn_re_ycord[i], ds.vn_re_zcord[i], ds.vn_sim_xcord[i], ds.vn_sim_ycord[i], ds.vn_sim_zcord[i])
    vn_err.append(percdif)

er_err  = []
for i in range(len(ds.er_re_xcord)):
    percdif = pos_percentage_diff(ds.er_re_xcord[i], ds.er_re_ycord[i], ds.er_re_zcord[i], ds.er_sim_xcord[i], ds.er_sim_ycord[i], ds.er_sim_zcord[i])
    er_err.append(percdif)

ma_err = []
for i in range(len(ds.ma_re_xcord)):
    percdif = pos_percentage_diff(ds.ma_re_xcord[i], ds.ma_re_ycord[i], ds.ma_re_zcord[i], ds.ma_sim_xcord[i], ds.ma_sim_ycord[i], ds.ma_sim_zcord[i])
    ma_err.append(percdif)

jp_err = []
for i in range(len(ds.jp_re_xcord)):
    percdif = pos_percentage_diff(ds.jp_re_xcord[i], ds.jp_re_ycord[i], ds.jp_re_zcord[i], ds.jp_sim_xcord[i], ds.jp_sim_ycord[i], ds.jp_sim_zcord[i])
    jp_err.append(percdif)

sa_err = []
for i in range(len(ds.sa_re_xcord)):
    percdif = pos_percentage_diff(ds.sa_re_xcord[i], ds.sa_re_ycord[i], ds.sa_re_zcord[i], ds.sa_sim_xcord[i], ds.sa_sim_ycord[i], ds.sa_sim_zcord[i])
    sa_err.append(percdif)

ur_err = []
for i in range(len(ds.ur_re_xcord)):
    percdif = pos_percentage_diff(ds.ur_re_xcord[i], ds.ur_re_ycord[i], ds.ur_re_zcord[i], ds.ur_sim_xcord[i], ds.ur_sim_ycord[i], ds.ur_sim_zcord[i])
    ur_err.append(percdif)

ne_err = []
for i in range(len(ds.ne_re_xcord)):
    percdif = pos_percentage_diff(ds.ne_re_xcord[i], ds.ne_re_ycord[i], ds.ne_re_zcord[i], ds.ne_sim_xcord[i], ds.ne_sim_ycord[i], ds.ne_sim_zcord[i])
    ne_err.append(percdif)

oumua_err= []
for i in range(len(ds.om_xcord)):
    percdif = pos_percentage_diff(ds.om_xcord[i], ds.om_ycord[i], ds.om_zcord[i], ds.om_sim_xcord[i], ds.om_sim_ycord[i], ds.om_sim_zcord[i])
    oumua_err.append(percdif)


oumua_rad = []
for i in range(len(ds.om_sim_xcord)):
    oumua_rad.append(radial_dist(ds.om_sim_xcord[i], ds.om_sim_ycord[i], ds.om_sim_zcord[i]))

mer_rad = []
for i in range(len(ds.me_sim_xcord)):
    mer_rad.append(radial_dist(ds.me_sim_xcord[i], ds.me_sim_ycord[i], ds.me_sim_zcord[i]))

vn_rad = []
for i in range(len(ds.vn_sim_xcord)):
    vn_rad.append(radial_dist(ds.vn_sim_xcord[i], ds.vn_sim_ycord[i], ds.vn_sim_zcord[i]))

er_rad = []
for i in range(len(ds.er_sim_xcord)):
    er_rad.append(radial_dist(ds.er_sim_xcord[i], ds.er_sim_ycord[i], ds.er_sim_zcord[i]))

ma_rad = []
for i in range(len(ds.ma_sim_xcord)):
    ma_rad.append(radial_dist(ds.ma_sim_xcord[i], ds.ma_sim_ycord[i], ds.ma_sim_zcord[i]))

jp_rad = []
for i in range(len(ds.jp_sim_xcord)):
    jp_rad.append(radial_dist(ds.jp_sim_xcord[i], ds.jp_sim_ycord[i], ds.jp_sim_zcord[i]))

time = np.linspace(1,1921,1921)

plt.figure()
plt.subplot(211)
plt.plot(time, mer_err, label  = "Mercury",color="grey" )
plt.plot(time, vn_err, label = "Venus", color="orange" )
plt.plot(time, er_err, label = "Earth", color="lightblue")
plt.plot(time, ma_err, label = "Mars",  color="red")
plt.plot(time, jp_err, label = "Jupiter",color="green" )
plt.plot(time, sa_err, label = "Saturn", color="beige" )
plt.plot(time, ur_err, label = "Uranus", color="cyan")
plt.plot(time, ne_err, label = "Neptune", color="blue")
plt.suptitle("Errors of Simulation versus Real Data")
plt.xlabel("Time ($Hours$)")
plt.ylabel("Percentage Error")
plt.legend()

plt.subplot(212)
plt.plot(time, oumua_err, label = "Oumuamua", color  = "hotpink")
plt.xlabel("Time ($Hours$)")
plt.ylabel("Oumuamua Percentage Error")
plt.legend()

plt.tight_layout()
plt.show()


plt.figure()
plt.subplot(211)
plt.plot(oumua_rad, oumua_err, label = "Oumuamua", color = "hotpink")
plt.title("Oumuamua Error vs Radial Distance")
plt.xlabel("Radial Distance ($Km$)")
plt.ylabel("Oumuamua Percentage Error")
plt.legend()

plt.subplot(212)
plt.plot(time, mer_rad, label  = "Mercury",color="grey" )
plt.plot(time, vn_rad, label = "Venus", color="orange" )
plt.plot(time, er_rad, label = "Earth", color="lightblue")
plt.plot(time, ma_rad, label = "Mars",  color="red")
# plt.plot(time, jp_rad, label = "Jupiter",color="green" )
plt.suptitle("Errors of Simulation versus Real Data")
plt.xlabel("Time ($Hours$)")
plt.ylabel("Radial Distance ($Km$)")
plt.legend()

plt.tight_layout()
plt.show()

