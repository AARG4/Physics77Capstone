import numpy as np
import csv

om_xcord = []
om_ycord = []
om_zcord = []
om_xvel = []
om_yvel = []
om_zvel = []
om_time = []

f = open("oumuamua_jpl_dataset.txt", "r")
f.readline()
for line in f:
    wholeset = line.split()
    om_xcord.append(float(wholeset[5]))
    om_ycord.append(float(wholeset[6]))
    om_zcord.append(float(wholeset[7]))
    om_xvel.append(float(wholeset[8]))
    om_yvel.append(float(wholeset[9]))
    om_zvel.append(float(wholeset[10]))
f.close()

om_sim = []
om_sim_xcord = []
om_sim_ycord = []
om_sim_zcord = []
om_sim_xvel = []
om_sim_yvel = []
om_sim_zvel = []
om_sim_time = []

f_csv = open('Simulation_CSVfiles_Asteroid/Oumuamua Asteroid.csv', 'r')
csv_reader = csv.reader( f_csv, delimiter = ',' )
next(csv_reader)

for row in csv_reader:
    om_sim_xcord.append(float(row[1]))
    om_sim_ycord.append(float(row[2]))
    om_sim_zcord.append(float(row[3]))
    om_sim_xvel.append(float(row[4]))
    om_sim_yvel.append(float(row[5]))
    om_sim_zvel.append(float(row[6]))
f_csv.close()

mer_real = []
me_re_xcord = []
me_re_ycord = []
me_re_zcord = []
me_re_xvel = []
me_re_yvel = []
me_re_zvel = []
me_re_time = []

f = open("Planetary Data Set/Mercury_Dataset.txt", "r")
f.readline()
for line in f:
    wholeset = line.split()
    me_re_xcord.append(float(wholeset[5]))
    me_re_ycord.append(float(wholeset[6]))
    me_re_zcord.append(float(wholeset[7]))
    me_re_xvel.append(float(wholeset[8]))
    me_re_yvel.append(float(wholeset[9]))
    me_re_zvel.append(float(wholeset[10]))
f.close()


mer_sim = []
me_sim_xcord = []
me_sim_ycord = []
me_sim_zcord = []
me_sim_xvel = []
me_sim_yvel = []
me_sim_zvel = []
me_sim_time = []

f_csv = open('Simulation_CSVfiles_Asteroid/Mercury.csv', 'r')
csv_reader = csv.reader( f_csv, delimiter = ',' )
next(csv_reader)

for row in csv_reader:
    me_sim_xcord.append(float(row[1]))
    me_sim_ycord.append(float(row[2]))
    me_sim_zcord.append(float(row[3]))
    me_sim_xvel.append(float(row[4]))
    me_sim_yvel.append(float(row[5]))
    me_sim_zvel.append(float(row[6]))
f_csv.close()

ven_real = []
vn_re_xcord = []
vn_re_ycord = []
vn_re_zcord = []
vn_re_xvel = []
vn_re_yvel = []
vn_re_zvel = []
vn_re_time = []
f = open("Planetary Data Set/Venus_Dataset.txt", "r")
f.readline()
for line in f:
    wholeset = line.split()
    vn_re_xcord.append(float(wholeset[5]))
    vn_re_ycord.append(float(wholeset[6]))
    vn_re_zcord.append(float(wholeset[7]))
    vn_re_xvel.append(float(wholeset[8]))
    vn_re_yvel.append(float(wholeset[9]))
    vn_re_zvel.append(float(wholeset[10]))
f.close()


ven_sim = []
vn_sim_xcord = []
vn_sim_ycord = []
vn_sim_zcord = []
vn_sim_xvel = []
vn_sim_yvel = []
vn_sim_zvel = []
vn_sim_time = []
f_csv = open('Simulation_CSVfiles_Asteroid/Venus.csv', 'r')
csv_reader = csv.reader( f_csv, delimiter = ',' )
next(csv_reader)

for row in csv_reader:
    vn_sim_xcord.append(float(row[1]))
    vn_sim_ycord.append(float(row[2]))
    vn_sim_zcord.append(float(row[3]))
    vn_sim_xvel.append(float(row[4]))
    vn_sim_yvel.append(float(row[5]))
    vn_sim_zvel.append(float(row[6]))
f_csv.close()

ear_real = []
er_re_xcord = []
er_re_ycord = []
er_re_zcord = []
er_re_xvel = []
er_re_yvel = []
er_re_zvel = []
er_re_time = []
f = open("Planetary Data Set/Earth_Dataset.txt", "r")
f.readline()
for line in f:
    wholeset = line.split()
    er_re_xcord.append(float(wholeset[5]))
    er_re_ycord.append(float(wholeset[6]))
    er_re_zcord.append(float(wholeset[7]))
    er_re_xvel.append(float(wholeset[8]))
    er_re_yvel.append(float(wholeset[9]))
    er_re_zvel.append(float(wholeset[10]))
f.close()


ear_sim = []
er_sim_xcord = []
er_sim_ycord = []
er_sim_zcord = []
er_sim_xvel = []
er_sim_yvel = []
er_sim_zvel = []
er_sim_time = []
f_csv = open('Simulation_CSVfiles_Asteroid/Earth.csv', 'r')
csv_reader = csv.reader( f_csv, delimiter = ',' )
next(csv_reader)

for row in csv_reader:
    er_sim_xcord.append(float(row[1]))
    er_sim_ycord.append(float(row[2]))
    er_sim_zcord.append(float(row[3]))
    er_sim_xvel.append(float(row[4]))
    er_sim_yvel.append(float(row[5]))
    er_sim_zvel.append(float(row[6]))
f_csv.close()

mar_real = []
ma_re_xcord = []
ma_re_ycord = []
ma_re_zcord = []
ma_re_xvel = []
ma_re_yvel = []
ma_re_zvel = []
ma_re_time = []
f = open("Planetary Data Set/Mars_Dataset.txt", "r")
f.readline()
for line in f:
    wholeset = line.split()
    ma_re_xcord.append(float(wholeset[5]))
    ma_re_ycord.append(float(wholeset[6]))
    ma_re_zcord.append(float(wholeset[7]))
    ma_re_xvel.append(float(wholeset[8]))
    ma_re_yvel.append(float(wholeset[9]))
    ma_re_zvel.append(float(wholeset[10]))
f.close()

mar_sim = []
ma_sim_xcord = []
ma_sim_ycord = []
ma_sim_zcord = []
ma_sim_xvel = []
ma_sim_yvel = []
ma_sim_zvel = []
ma_sim_time = []
f_csv = open('Simulation_CSVfiles_Asteroid/Mars.csv', 'r')
csv_reader = csv.reader( f_csv, delimiter = ',' )
next(csv_reader)

for row in csv_reader:
    ma_sim_xcord.append(float(row[1]))
    ma_sim_ycord.append(float(row[2]))
    ma_sim_zcord.append(float(row[3]))
    ma_sim_xvel.append(float(row[4]))
    ma_sim_yvel.append(float(row[5]))
    ma_sim_zvel.append(float(row[6]))
f_csv.close()

jup_real = []
jp_re_xcord = []
jp_re_ycord = []
jp_re_zcord = []
jp_re_xvel = []
jp_re_yvel = []
jp_re_zvel = []
jp_re_time = []
f = open("Planetary Data Set/Jupiter_Dataset.txt", "r")
f.readline()
for line in f:
    wholeset = line.split()
    jp_re_xcord.append(float(wholeset[5]))
    jp_re_ycord.append(float(wholeset[6]))
    jp_re_zcord.append(float(wholeset[7]))
    jp_re_xvel.append(float(wholeset[8]))
    jp_re_yvel.append(float(wholeset[9]))
    jp_re_zvel.append(float(wholeset[10]))
f.close()


jup_sim = []
jp_sim_xcord = []
jp_sim_ycord = []
jp_sim_zcord = []
jp_sim_xvel = []
jp_sim_yvel = []
jp_sim_zvel = []
jp_sim_time = []
f_csv = open('Simulation_CSVfiles_Asteroid/Jupiter.csv', 'r')
csv_reader = csv.reader( f_csv, delimiter = ',' )
next(csv_reader)

for row in csv_reader:
    jp_sim_xcord.append(float(row[1]))
    jp_sim_ycord.append(float(row[2]))
    jp_sim_zcord.append(float(row[3]))
    jp_sim_xvel.append(float(row[4]))
    jp_sim_yvel.append(float(row[5]))
    jp_sim_zvel.append(float(row[6]))
f_csv.close()


sat_real = []
sa_re_xcord = []
sa_re_ycord = []
sa_re_zcord = []
sa_re_xvel = []
sa_re_yvel = []
sa_re_zvel = []
sa_re_time = []
f = open("Planetary Data Set/Saturn_Dataset.txt", "r")
f.readline()
for line in f:
    wholeset = line.split()
    sa_re_xcord.append(float(wholeset[5]))
    sa_re_ycord.append(float(wholeset[6]))
    sa_re_zcord.append(float(wholeset[7]))
    sa_re_xvel.append(float(wholeset[8]))
    sa_re_yvel.append(float(wholeset[9]))
    sa_re_zvel.append(float(wholeset[10]))
f.close()

sat_sim = []
sa_sim_xcord = []
sa_sim_ycord = []
sa_sim_zcord = []
sa_sim_xvel = []
sa_sim_yvel = []
sa_sim_zvel = []
sa_sim_time = []
f_csv = open('Simulation_CSVfiles_Asteroid/Saturn.csv', 'r')
csv_reader = csv.reader( f_csv, delimiter = ',' )
next(csv_reader)

for row in csv_reader:
    sa_sim_xcord.append(float(row[1]))
    sa_sim_ycord.append(float(row[2]))
    sa_sim_zcord.append(float(row[3]))
    sa_sim_xvel.append(float(row[4]))
    sa_sim_yvel.append(float(row[5]))
    sa_sim_zvel.append(float(row[6]))
f_csv.close()

ura_real = []
ur_re_xcord = []
ur_re_ycord = []
ur_re_zcord = []
ur_re_xvel = []
ur_re_yvel = []
ur_re_zvel = []
ur_re_time = []
f = open("Planetary Data Set/Uranus_Dataset.txt", "r")
f.readline()
for line in f:
    wholeset = line.split()
    ur_re_xcord.append(float(wholeset[5]))
    ur_re_ycord.append(float(wholeset[6]))
    ur_re_zcord.append(float(wholeset[7]))
    ur_re_xvel.append(float(wholeset[8]))
    ur_re_yvel.append(float(wholeset[9]))
    ur_re_zvel.append(float(wholeset[10]))
f.close()

ura_sim = []
ur_sim_xcord = []
ur_sim_ycord = []
ur_sim_zcord = []
ur_sim_xvel = []
ur_sim_yvel = []
ur_sim_zvel = []
ur_sim_time = []
f_csv = open('Simulation_CSVfiles_Asteroid/Uranus.csv', 'r')
csv_reader = csv.reader( f_csv, delimiter = ',' )
next(csv_reader)

for row in csv_reader:
    ur_sim_xcord.append(float(row[1]))
    ur_sim_ycord.append(float(row[2]))
    ur_sim_zcord.append(float(row[3]))
    ur_sim_xvel.append(float(row[4]))
    ur_sim_yvel.append(float(row[5]))
    ur_sim_zvel.append(float(row[6]))
f_csv.close()

nep_real = []
ne_re_xcord = []
ne_re_ycord = []
ne_re_zcord = []
ne_re_xvel = []
ne_re_yvel = []
ne_re_zvel = []
ne_re_time = []
f = open("Planetary Data Set/Neptune_Dataset.txt", "r")
f.readline()
for line in f:
    wholeset = line.split()
    ne_re_xcord.append(float(wholeset[5]))
    ne_re_ycord.append(float(wholeset[6]))
    ne_re_zcord.append(float(wholeset[7]))
    ne_re_xvel.append(float(wholeset[8]))
    ne_re_yvel.append(float(wholeset[9]))
    ne_re_zvel.append(float(wholeset[10]))
f.close()

nep_sim = []
ne_sim_xcord = []
ne_sim_ycord = []
ne_sim_zcord = []
ne_sim_xvel = []
ne_sim_yvel = []
ne_sim_zvel = []
ne_sim_time = []
f_csv = open('Simulation_CSVfiles_Asteroid/Neptune.csv', 'r')
csv_reader = csv.reader( f_csv, delimiter = ',' )
next(csv_reader)

for row in csv_reader:
    ne_sim_xcord.append(float(row[1]))
    ne_sim_ycord.append(float(row[2]))
    ne_sim_zcord.append(float(row[3]))
    ne_sim_xvel.append(float(row[4]))
    ne_sim_yvel.append(float(row[5]))
    ne_sim_zvel.append(float(row[6]))
f_csv.close()



