#GlowScript 2.1 VPython
#Safford, Vega, Yancey
from __future__ import division, print_function
from visual import *
scene.width = scene.height = 800

G = 6.7e-11
earthm = 6e24
apollom = 15e3
mmoon = 7e22
deltat = 100

earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.blue)
apollo = sphere(pos=vector(-10*earth.radius, 0,0), radius=1e6, color=color.red, make_trail=True)
moon = sphere(pos=vector(4e8,0,0), radius=1.75e6, color=color.white)
vapollo = vector(0,2900,0)
papollo = apollom*vapollo
t = 2
scene.autoscale = False ##turn off automatic camera zoom

r_from_p = (apollo.pos - earth.pos)
r_mag = mag(r_from_p)
r_hat = -(r_from_p)/r_mag
r_squared = mag2(r_from_p)
F_grav_earth = G*apollom*earthm/(mag(apollo.pos-earth.pos)**2)*r_hat


r_from_m = (apollo.pos - moon.pos)
r_mag_m = mag(r_from_m)
r_hat_m = -(r_from_m)/r_mag_m
r_squared = mag2(r_from_m)
F_grav_moon = (G*apollom*mmoon/(mag(apollo.pos-moon.pos)**2))*r_hat_m

print(papollo)
sf = 0.25
parr = arrow(pos = papollo , axis = (0,3,0), color = color.yellow)


farr = arrow(pos = r_from_p , axis = F_grav_earth*10000, color = color. red)    


  
while t < 10*365*24*60*60*60:
    rate(100)
    F_grav_earth =  (G*apollom*earthm/(mag(apollo.pos-earth.pos)**2))*r_hat
    F_grav_moon = (G*apollom*mmoon/(mag(apollo.pos-moon.pos)**2))*r_hat_m
    
    papollo = papollo + (F_grav_moon + F_grav_earth)*deltat
    apollo.pos = apollo.pos + (papollo/apollom)*deltat

    ## earth Stuff
    r_hat = -(apollo.pos-earth.pos)/mag(apollo.pos-earth.pos)
    
    #r_from_p = (apollo.pos - earth.pos)
    #r_mag = mag(r_from_p)
    #r_hat = -(r_from_p)/r_mag

    ##Moon Stuff
    r_hat_m = -(apollo.pos-moon.pos)/mag(apollo.pos-moon.pos)
    #r_mag_m = mag(r_from_m)
    #r_hat_m = -(r_from_m)/r_mag_m
    
    t = t+deltat
    parr.pos = apollo.pos
    parr.axis = papollo * sf
    farr.pos = apollo.pos
    farr.axis = F_grav_earth * 10000

    if r_mag < earth.radius:
        break ## exit from the loop
    elif r_mag_m < moon.radius:
        break ## exit from the loop



#3.0, initial speed leading to crashing into the Moon = 3289 m/s
#The initial speed leading to an elliptical orbit around earth and Moon = 3320 m/s
#The initial speed yielding a figure-8 orbit around Moon before return to earth = 3273.7 m/s
#The initial speed that produces different/ interesting orbit = 3267 m/s
#A very large time step gives a very inaccurate orbit since the velocity is changing instantaneously with respect to these time steps
