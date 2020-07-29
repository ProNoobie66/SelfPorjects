# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 21:20:53 2020

@author: Rohit
"""
#assingment 1 my style 
import numpy as np
import matplotlib.pylab as plt

dt = 0.1

def projectile(v,angle):
    t = 0
    tlist = [t]
    #x component
    xlist = [0]
    x = 0
    vx = v*np.cos(angle)
    cd = 0.005
    ax = -cd*vx*vx
    vxlist = [vx]
    # y component
    ylist = [0]
    y = 0
    vy = v*np.sin(angle)
    g = 9.8
    ay = -cd*vy*vy
    vylist = [vy]
    while y >= 0:
        ax = -cd*vx*vx
        vx = vx + ax*dt
        x = x + vx*dt
        ay = -cd*vy*vy
        vy = vy - g*dt + ay*dt
        y = y + vy*dt
        t=t+dt
        if y<0:
            break
        tlist.append(t)
        vxlist.append(vx)
        vylist.append(vy)
        xlist.append(x)
        ylist.append(y)
    #print(x,y,"\n")
    #print the values of coordinate
    return xlist,ylist#,vxlist,vylist,tlist
    
x1,y1 = projectile(30, np.pi/3)
x2,y2 = projectile(80, np.pi/4)
x3,y3 = projectile(80, np.pi/2)
x4,y4 = projectile(80, np.pi/3)

#plot
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
#plt.plot(t1,vx1,label="x velocity")
#plt.plot(t1,vy1,label = "y velocity")
#plt.xlabel("t")
#plt.ylabel("v")
plt.legend()
plt.show()
