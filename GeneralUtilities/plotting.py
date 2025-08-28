#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 14:51:45 2025

@author: nayandusoruth
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

""" Plotting functions
Some general plotting functions using matplot lib
"""
# new plotter function
class plotter():
# utility methods
    # constructor method ----------------------------
    def __init__(self, markWidth=0.8, markArea=12, gridCol='k', gridSty='-',gridWid=0.1):
        # setup figure/axes
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()
        
        # setup standard formatting variables
        self.markerWidth = markWidth
        self.markerArea = markArea
        
        self.gridColor = gridCol
        self.gridStyle = gridSty
        self.gridWidth = gridWid
        
    # display figure method
    def display(self):
        plt.show()
        
    # save figure method
        
# figure "setup" methods ----------------------------
    
    # axis labels method
    def axisLabels(self, xLabel="xData", yLabel="yData"):
        self.ax.set_xlabel(xLabel)
        self.ax.set_ylabel(yLabel)
        
    # axis ticks methods
    def axisTicks(self, xTicks, yTicks):
        # setup axis ticks
        self.ax.set_xticks(xTicks)
        self.ax.set_yticks(yTicks)
        
    # gridline setup method
    def gridline(self):
        self.ax.grid(color=self.gridColor, linestyle=self.gridStyle, linewidth=self.gridWidth)
    # 
    
# plotting methods ---------------------------------

    # base scatter method
    def scatter(self, xData, yData, marker = 'x', color='k'):
        self.ax.scatter(xData, yData, marker = 'x', color=color, s=self.markerArea, linewidths=self.markerWidth)
    
    # scatter w/yAxis errorbars method
    
    # scatter w/xAxis errorbars method
    
    # scatter w/xyAxis errorbars method
    
    # base histogram method
    
    # histogram w/yAxis errorbars method










# testing -----------------------------------------------------------------------------------------------------------------

xTicks = np.arange(0, 10, 2)
yTicks = np.arange(0,5,1)

xData = np.arange(0, 10, 1)
yData = np.arange(0, 5, 0.5)

xDataErr = np.full(10, 0.25)
yDataErr = np.full(10, 0.25)


plotter = plotter()

plotter.axisLabels()
plotter.gridline()
plotter.axisTicks(xTicks, yTicks)
plotter.scatter(xData, yData)

plotter.display()




# old functions -----------------------------------------------------------------------------------------------------------------

def scatter2D(xData, yData, xLabel="xData", yLabel="yData", gridlines=True, markerArea = 12, markerWidth = 0.8, color = "k"):
    """Plotting function - simple scatter plot function for xData, yData - intended for quick barebones plotting"""
    # setup figure/axes
    fig = plt.figure()
    ax = fig.add_subplot()
    
    # title axes
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    
    # setup gridlines if desired
    if(gridlines):
        ax.grid(color='k', linestyle='-', linewidth=0.1)
            

    # plot values
    ax.scatter(xData, yData, marker = 'x', color=color, s=markerArea, linewidths=markerWidth)
     
    # plot and return
    plt.show()    
    return fig

def scatter2DTicks(xData, yData, xTicks, yTicks, xLabel="xData", yLabel="yData", gridlines=True, markerArea = 12, markerWidth = 0.8, color = "k"):
    """Plotting function - simple scatter plot function for xData, yData - includes custom x/y axis ticks- intended for quick barebones plotting"""
    # setup figure/axes
    fig = plt.figure()
    ax = fig.add_subplot()
    
    # title axes
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    
    # setup gridlines if desired
    if(gridlines):
        ax.grid(color='k', linestyle='-', linewidth=0.1)
            
    # setup axis ticks
    ax.set_xticks(xTicks)
    ax.set_yticks(yTicks)

    # plot values
    ax.scatter(xData, yData, marker = 'x', color=color, s=markerArea, linewidths=markerWidth)
     
    # plot and return
    plt.show()    
    return fig

def histogram(xData, bins = 10, label="data", gridlines=True, markerArea = 12, markerWidth = 0.8, color = "r"):
    """Plotting function - simple scatter plot function for xData, yData - intended for quick barebones plotting"""
    # setup figure/axes
    fig = plt.figure()
    ax = fig.add_subplot()
    
    # title axes
    ax.set_xlabel(label)
    
    # setup gridlines if desired
    if(gridlines):
        ax.grid(color='k', linestyle='-', linewidth=0.1)
            

    # plot values
    ax.hist(xData, bins = bins, color=color)# s=markerArea, linewidths=markerWidth)
     
    # plot and return
    plt.show()    
    return fig
