from __future__ import division, print_function
from visual import *
from visual.graph import *


# VALUES FOR EARTH
earth= sphere( pos= vector(0,0,0), radius=6.4e6, color=color.blue)
earthm=6e24
earthv= vector(1,0,0)
earthp = earthm*earthv



# VLAUES FOR APOLLO
apollo = sphere (pos=vector( -10*earth.radius,0,0), radius=1e6, color=color.red, make_trail=True)
apollom= 15e3
apollov= vector(0,2e3,0)
apollop=apollom*apollov


t=0
G=(6.7e-11)
deltat=60
r=apollo.pos-earth.pos
rhat=r/mag(r)
parrow= arrow(pos=apollo.pos, axis=apollop, color=color.blue)
farrow= arrow(pos=apollo.pos, axis=-(G*apollom*earthm/mag(r)**2*-rhat),color=color.yellow)
scale=0.5
scalef=4000
print(apollop)
scene.autoscale= False ##turn off automatic camera zoom

while t < 10*365*24*60*60:
    rate(300)
    earthp = earthm*earthv
    apollo.pos = apollo.pos +  ( apollop/apollom)*deltat
    earth.pos= vector(0,0,0)
    parrow.pos=apollo.pos
    parrow.axis=apollop*scale
    r=apollo.pos-earth.pos
    rhat=r/mag(r)
    farrow.pos= apollo.pos
    farrow.axis= (G*apollom*earthm/mag(r)**2*-rhat)*scalef
    
    fonapollo=(G*apollom*earthm/mag(r)**2*-rhat)
    apollop= apollop + (fonapollo*deltat)
    fonearth= -fonapollo
    earthp= earthp + fonearth * deltat
    
    
    if mag(r) < earth.radius:
        break ## exit from the loop
