# Linton, Safford, Vega
#VP 07 

from __future__ import division, print_function
from visual import *
from visual.graph import *
scene.width = 400
scene.height = 760
## constants and data
g = 9.81
mball = 100
L0 = 0.26
ks =  15536
deltat = .01
funct = gcurve(title = 'Time vs Spring Oscillations', xtitle = 'Time (s)', ytitle = 'Distance from ceiling',color=color.yellow)
## objects (origin is at ceiling)
ceiling = box(pos=vector(0,0,0), length=0.2, height=0.01, width=0.2)
ball = sphere(pos=vector(0,-0.3,0), radius=0.025,
color=color.orange,make_trail=True)
spring = helix(pos=ceiling.pos, axis=ball.pos-ceiling.pos,
color=color.cyan, thickness=.003, coils=40, radius=0.010)
## initial values
pball = mball*vector(0,0,0)
Fgrav = mball*g*vector(1,-1,-1)
t = 0
#initial stretch of spring with mass attached
#stretch = Fgrav/ks
#print(stretch)
#ball.pos = ball.pos+stretch
#print(stretch+ball.pos)
#spring.axis = ball.pos-ceiling.pos
#print(spring.axis)
## improve the display
scene.autoscale = False ## turn off automatic camera zoom
scene.center = vector(0,-L0,0) ## move camera down
scene.waitfor('click') ## wait for a mouse click
## calculation loop
while t<10:
        rate(30)
        L = ball.pos-spring.pos
        Lhat = L/mag(L)
        s = mag(L)-L0
        Fspring = -ks*s*Lhat
        Fnet = Fgrav+Fspring
        #print(Fnet)
        acceleration = Fnet/mball
        pball = pball + Fnet *deltat
        ball.pos = ball.pos + (pball/mball)*deltat
        print(ball.pos)
        spring.axis = ball.pos - ceiling.pos
        #print(spring.axis)
        #while abs(ball.pos)>= 0.4635:
           # L_new = spring.axis
        #print(L_new)
        t = t + deltat
# Graph of ball's motion
        funct.plot(pos = (t,ball.pos.y))
