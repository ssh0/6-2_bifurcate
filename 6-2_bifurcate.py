#!/usr/bin/env python 
# coding:utf-8
#
# written by Shotaro Fujimoto, May 2014.
""" 計算機実習
問題6.2
プログラムを実行すると、パラメータの設定ダイアログが開き、
OKボタンを押すとグラフが描画される。
いろいろなrについてxの値をプロットする。
"""
from math import *
import SetParameter
import myplot_bifurcation

def assignment():
    x0 = float(run.entry[0].get())
    ntransient = int(run.entry[1].get())
    nplot = int(run.entry[2].get())
    r0 = float(run.entry[3].get())
    rmax = 1.0
    dr = float(run.entry[4].get())
    def func(x_i, r):
        return 4.0*r*x_i*(1.0-x_i)
    run.quit()
    myplot_bifurcation.Plot(func, x0, ntransient, nplot, r0, rmax, dr)
    
if __name__ == '__main__':
    run = SetParameter.SetParameter()
    parameters = [{'x0':0.3}, {'ntransient':1000}, {'nplot':50}, {'r0':0.7}, {'dr':0.0005}]
    run.show_setting_window(parameters, {'OK':assignment})

