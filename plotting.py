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

def scatter2D(xData, yData, xLabel="xData", yLabel="yData", gridlines=True, markerArea = 12, markerWidth = 0.8):
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
    ax.scatter(xData, yData, marker = 'x', color="k", s=markerArea, linewidths=markerWidth)
     
    # plot and return
    plt.show()    
    return fig