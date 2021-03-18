# -*- coding: utf-8  -*-
# -*- author: jokker -*-


#发现率y
#误报率x

import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def C(X, Y):
    #print('C')
    zero = X*Y/(1-X) > 5
    #print(zero)
    c = np.array([(24 - 4* np.ceil(x*y/(1-x))) for x,y in zip(X,Y)])
    #print(c.shape)
    c[zero] = 0
    return c

def score(x,y):
    #print('score')
    zero = y>x
    #print(zero)
    z = 65*y + 10*(1-x) + C(x,y)
    z[zero] = 0
    print(type(z))
    return z

if __name__=="__main__":
    fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    ax=Axes3D(fig)
    X = np.arange(0.1, 1, 0.001)
    Y = np.arange(0.1, 1, 0.001)
    #print(X)
    X, Y = np.meshgrid(X, Y)
    Z = score(X,Y)
    pos = np.unravel_index(np.argmin(Z),Z.shape)
    print(Z.shape)
    print(np.argmax(Z))
    print(pos)
    #print(Z)
    ax.plot_surface(X, Y, Z,  cmap=plt.cm.coolwarm)
    ax.set_xlabel('x label', color='r')
    ax.set_ylabel('y label', color='g')
    ax.set_zlabel('z label', color='b')
    plt.show()
