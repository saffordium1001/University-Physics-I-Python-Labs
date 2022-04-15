# Linton, Safford, Vega
#VP 07 

from __future__ import division, print_function
from visual import *
from visual.graph import *
scene.width = 400
scene.height = 760

## constants and data
g = 9.81
mball = 0.03
L0 = 0.26
ks =  1.8
deltat = .01
funct1 = gcurve(title = 'Time vs Spring Oscillations', xtitle = 'Time (s)', ytitle = 'Distance from ceiling')
funct2 = gcurve(title = 'Time vs Spring Oscillations', xtitle = 'Time (s)', ytitle = 'Distance from ceiling')
funct3 = gcurve(title = 'Time vs Spring Oscillations', xtitle = 'Time (s)', ytitle = 'Distance from ceiling')
funct4 = gcurve(title = 'Time vs Spring Oscillations', xtitle = 'Time (s)', ytitle = 'Distance from ceiling')


## objects (origin is at ceiling)
ceiling = box(pos=vector(0,0,0), length=0.2, height=0.01, width=0.2)
ball = sphere(pos=vector(0,-0.3,0), radius=0.025,
color=color.orange,make_trail=True)
spring = helix(pos=ceiling.pos, axis=ball.pos-ceiling.pos,
color=color.cyan, thickness=.003, coils=40, radius=0.010)

## initial values
pball = mball*vector(0,0,0)
Fgrav = mball*g*vector(0,-1,0)
t = 0
L = ball.pos-spring.pos
Lhat = L/mag(L)
s = mag(L)-L0
Fspring = -ks*s*Lhat
Fnet = Fgrav+Fspring

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

# Create arrow to model the momentum of the ball
momentum_ball_arrow = arrow(pos=pball, axis = ball.pos , color = color.red, fixedwidth = True, shaftwidth = 0.01, shaftlength = 0.01)

#Create arrow to model the net force on the ball
net_force_ball_arrow = arrow(pos = ball.pos, axis = Fnet, color = color.blue, fixedwidth = True, shaftwidth=0.01, shaftlength = 0.01)



#Create line to account for kinetic energy (spring)


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
        pball = (pball + Fnet *deltat)
        vball = mag(pball/mball)
        ball.pos = ball.pos + (pball/mball)*deltat
        #print(ball.pos)
        spring.axis = ball.pos - ceiling.pos
        #print(spring.axis)
        #while abs(ball.pos)>= 0.4635:
           # L_new = spring.axis
        #print(L_new)
        momentum_ball_arrow.pos = ball.pos
        momentum_ball_arrow.axis =  pball*0.01
        net_force_ball_arrow.pos = ball.pos
        net_force_ball_arrow.axis = Fnet*0.001  
        t = t + deltat
       #Create line to account for elastic energy (spring)
        elastic_spring_potential = 0.5 * ks * pow(s,2)
        #print(elastic_spring_potential)
        # Create line to account for kinetic energy (spring)
        elastic_kinetic_energy = 0.5 * mball * pow(vball,2)
        #print(elastic_kinetic_energy)
        # Create line to account for kinetic energy (spring)
        total_energy = elastic_spring_potential + elastic_kinetic_energy
        #print(elastic_kinetic_energy)
# Create arrow to model the momentum of the ball
        #momentum_ball_arrow = arrow(pos =pball, axis = ball.pos-spring.pos , color = color.red)

#Create arrow to model the net force on the ball
        #net_force_ball_arrow = arrow(pos = ball.pos, axis = Fnet, color = color.blue, shaftwidth=0.001)
# Graph of ball's motion

        #funct.plot(pos = (t,ball.pos.y))
        f1 = funct1.plot(pos = (t,elastic_kinetic_energy), title = 'Spring Oscillation Behavior', xtitle = 'Time (seconds)',  color = color.blue, shape = round)
        f2 = funct2.plot(pos = (t,total_energy),  title = 'Spring Oscillation Behavior', xtitle = 'Time (seconds)', color = color.green)
        f3 = funct3.plot(pos = (t,elastic_spring_potential),  title = 'Spring Oscillation Behavior', xtitle = 'Time (seconds)', color = color.red, dot = True)
        f4 = funct4.plot(pos = (t,ball.pos.y), title = 'Spring Oscillation Behavior', xtitle = 'Time (seconds)',  color = color.yellow)
