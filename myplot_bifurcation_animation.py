#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.
#

import matplotlib.pylab as plt
import matplotlib.animation as animation
import array as array
import numpy as np

fig = plt.figure()

def Plot(func, x0, ntransient, nplot, r0, rmax, dr):
    
    def callback(n):
        _Plot(func, r0+dr*n, x0, ntransient, nplot)

    plt.gca().set_xlim(r0,rmax)
    plt.gca().set_ylim(0,1)
    plt.xlabel(r'$r$', fontsize=16)
    plt.ylabel(r'$x$', fontsize=16)
    plt.title('Bifurcation Diagram')
    count=int((rmax-r0)/dr)
    animation.FuncAnimation(fig=fig, func=callback, frames=count + 1, repeat=False)
    plt.show()


def _Plot(function, r, x0, ntransient, nplot):
    n=ntransient+nplot*2
    x=array.array('f')
    x.append(x0)
    for i in range(n):
        x.append(function(x[i], r))
    plt.scatter([r]*nplot, x[ntransient+1:ntransient+nplot+1],
                color='r', s=0.1, marker='.'
               )
    plt.scatter([r]*nplot, x[ntransient+nplot+1:n+1],
                color='b', s=0.1, marker='.'
               )

