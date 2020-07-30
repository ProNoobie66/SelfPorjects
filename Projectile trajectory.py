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
    cd = 0.00560
    ax = -cd*vx*vx
    # y component
    ylist = [0]
    y = 0
    vy = v*np.sin(angle)
    g = 9.8
    ay = -cd*vy*vy
    while y >= 0:
        ax = -cd*vx*vx
        vx = vx + ax*dt
        x = x + vx*dt
        ay = -cd*vy*vy
        vy = vy - g*dt + ay*dt
        y = y + vy*dt
        t=t+dt
        tlist.append(t)
        xlist.append(x)
        ylist.append(y)
    return xlist,ylist,tlist

#UI
ans = 'Y'
while ans == "Y" or ans == "y":
    print("-----------------------Projectile under Air resistance-------------------------")
    vel = float(input("Enter the velocity of projectile\t"))
    ang = float(input("Enter the angle of projectile in degree\t")) 
    angle = ang * np.pi / 180
    x1,y1,t1 = projectile(vel, angle)
    h = round(max(y1),2)
    r = round(max(x1),2)
    t = round(max(t1),1)
    xy = max(h,r)
    #figure
    fig = plt.figure()
    fig.suptitle("Projectile Trajectory")
    ax = fig.add_subplot()
    ax.set_xlabel('Range(m)')
    ax.set_ylabel('Height(m)')
    ax.axis([0,xy+10,0,xy+10])
    ax.plot(x1,y1,"-.")
    fig.text(0.2,0.90,("Velocity = "+ str(vel) + "m/s Angle of launch = " + str(ang) + "\N{DEGREE SIGN}" ))
    fig.text(0.2,-0.05,("Range = "+ str(r) + "m Max height = " + str(h) + "m Time of flight = "+str(t)+"s"))
    plt.show()
    ans = input("Try again?[Y/N]")
print("-----------------------------Terminated---------------------------------------")