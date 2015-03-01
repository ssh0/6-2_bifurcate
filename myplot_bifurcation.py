#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""

Shotaro Fujimoto
"""
import matplotlib.pylab as plt
import numpy as np

def Plot(func, x0, ntransient, nplot, r0, rmax, dr):
    global x
    count = int((rmax-r0)/dr)
    fig = [_Plot(func, r0+dr*n, x0, ntransient, nplot) for n in range(count+1)]
    plt.gca().set_xlim(r0, rmax)
    plt.gca().set_ylim(np.min(x), np.max(x))
    plt.xlabel(r'$r$', fontsize=16)
    plt.ylabel(r'$x$', fontsize=16)
    plt.title('Bifurcation Diagram')
    plt.show()

def _Plot(function, r, x0, ntransient, nplot):
    global x
    n = ntransient + nplot*2
    x = [x0]
    for i in np.arange(n):
        x.append(function(x[i], r))
    x = np.array(x)
    plt.scatter([r]*nplot, x[ntransient+1:ntransient+nplot+1],
                color='r', s=0.1, marker='.'
               )
    plt.scatter([r]*nplot, x[ntransient+nplot+1:n+1],
                color='b', s=0.1, marker='.'
               )

