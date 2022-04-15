from __future__ import division, print_function
from visual import *
from visual.graph import *
from math import *
scene.width = 800

##Constants
massAu = (79+118)*1.7e-27
massAlpha = (2+2)*1.7e-27
qAlpha = 2*1.6e-19
qAu = 79*1.6e-19
oofpez = 9e9 ## one-over-four-pi-epsilon-zero
deltat = 1e-23


##Objects
Au = sphere(pos=vector(0,0,0), radius=8e-15, color=color.yellow, make_trail=True)
Alpha = sphere(pos=vector(-1e-13,0,0), radius=2e-15, color=color.red, make_trail=True)

#Initial Values
pAu = massAu*vector(0,0,0)
pAlpha = vector(1.043e-19,0,0)
pAlpha_mag = mag(pAlpha)
vAlpha_mag = pAlpha_mag/massAlpha
#Define permittivty constant
k = 1.38e-23
#Find change in momentum of the system
pAlpha_change = (k * qAlpha * qAu * 2 * Alpha.radius)/(pow(Alpha.radius,2) * (pAlpha_mag/massAlpha))
t = 0
#Scattering angle
scattering_angle = (pAlpha_change/pAlpha_mag)
#Determine the impact parameter - b
impact_parameter_part_one = (k * qAlpha * qAu)/(massAlpha*vAlpha_mag*vAlpha_mag)
impact_parameter_part_two = (sqrt((-sin(scattering_angle)/(sin(scattering_angle)))))
impact_parameter = impact_parameter_part_one * impact_parameter_part_two
#Maximum approach
maximum_approach = ((impact_parameter*cos((scattering_angle/2)))/(1-sin(scattering_angle/2)))
#print(scattering_angle) 
##Calculation Loop
while t < 1e-20:
    rate(1000)
    while (Alpha.pos - Au.pos) > maximum_approach
    Alpha.pos = Alpha.pos + (pAlpha/massAlpha)*deltat
    t = t + deltat
