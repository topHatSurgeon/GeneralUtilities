#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 11:17:10 2025

@author: nayandusoruth

Foreword:
This python file is meant to be a repository of assorted "general utilities" i've used/reused again and again. A personal library.
"""

import math
import scipy
import matplotlib.pyplot as plt
import numpy as np
import os
import time
import pandas as pd



""" File handling
A set of functions and utilities for handling files. This includes accessing CSV files, saving CSV, text, and image fig files, as well as creating new file paths
"""
# create new folder
def createFolder(directory, folderName):
    """File handling function - creates new folder at 'directory/folderName'"""
    newPath = str(directory + "/"+folderName)
    if (not os.path.exists(newPath)):
        os.makedirs(newPath)
    return newPath

# data function - reads CSV from filepath/filename - </verified/>
def getData(filePath, fileName):
    """File handling function - reads CSV from 'filepath/filename'"""
    # get data from directory/file and return to original directory
    curDir = os.getcwd()
    os.chdir(filePath)
    data = pd.read_csv(fileName + ".csv", skipinitialspace=True, sep=",", on_bad_lines='skip')
    os.chdir(curDir)

    # return
    return data

# utility function - saves dataframe as csv to filepath/filename.csv - </verified/>
def saveCSV(filepath, filename, dataFrame):
    """File handling function - saves dataframe as csv to filepath/filename.csv"""
    curDir = os.getcwd() # get the current directory
    os.chdir(filepath)
    path = filepath + filename + ".csv"
    dataFrame.to_csv(path)
    os.chdir(curDir)

# utility function - saves string text as txt to filepath/filename.txt"
def saveTxT(filepath, filename, text):
    """File handling function - saves string text as txt to filepath/filename.txt"""
    curDir = os.getcwd() # get the current directory
    os.chdir(filepath)
    
    file = open((filename + ".txt"), "")
    file.write(text)
    file.close()
    
    os.chdir(curDir)

# utility function - saves fig to directory with filename
def saveFigure(directory, fileName, fig):
    """File handling function - saves fig to directory with filename"""
    # go to desired directory
    curDir = os.getcwd() # get the current directory
    os.chdir(directory)

    # save figure to folder
    fig.savefig(fileName, dpi=300)
    
    # go back to original directory
    os.chdir(curDir)


""" progress class
a small utility class which acts as a "progress bar" - "packaged away" into it's own object for code reuse and legibility
"""
class progress():
    # constructor method - constructor for progress object - </verified/>
    def __init__(self, startIt, totalIt):
        """Constructor method - takes as arguments starting and total iterations of timer"""
        self.currentIteration = startIt
        self.totalIterations = totalIt
        
        # setup array of time stamps and corresponding iteration indices
        self.timeIndexes = np.array([0])
        self.times = np.array([time.time()])
    
    # utility function - cls() - clears txt console output - </verified/>
    def cls(self):
        """utility method - clears console"""
        os.system('cls' if os.name=='nt' else 'clear')
    
    # core function - increments progress object currentIteration - </verified/>
    def increment(self, increment=1):
        """Computational method - increments progress object iteration - takes as optional argument 'increment'"""
        self.currentIteration += increment
        
        # add new timestamp to timeIndexes and times
        self.timeIndexes = np.append(self.timeIndexes, self.currentIteration)
        self.times = np.append(self.times, time.time())
        
    # output function - displays current progress to console  - </verified/>
    def display(self, title="", percentDisplay=True, rounding=2):
        """Accessor method - displays current progress in console - takes as optional arguments the progress's 'title', wether to display it as a percentage, and the display rounding"""
        self.cls()
        if(percentDisplay):
            percent = round(100 * self.currentIteration / self.totalIterations, rounding)
            print(title, percent, "%", end="\r")
        else:
            print(title, self.currentIteration, " / ", self.totalIterations, end="\r")
    
    # utility function - returns total time elapsed by progress object
    def timeElapsed(self):
        """Accessor method - returns total time recorded"""
        return (self.times[len(self.times)-1] - self.times[0])
    
    
    
""" IO utilities
Assorted IO function utility functions
"""

# useful IO resources 
def IObool(text, default=True, ynDict = {"y":True, "n":False}):
    """IO function - general bool y/n question 'text' - returns boolean output"""
    return ynDict.get(input(text), default)

def IOint(text, default=1):
    """IO function - general int input question 'text' - returns int output"""
    inp = input(text)
    if(inp == "d"):
        return default
    return int(inp)

def IOfloat(text, default=0):
    """IO function - general float input question 'text' - returns float output"""
    inp = input(text)
    if(inp == "d"):
        return default
    return float(inp)

def IOsaveTxT(text, fileName):
    """IO function - queries where to save textfile"""
    filepath = input("save txt to filepath: ")
    saveTxT(filepath, fileName, text)
    
def IOsaveCSV(data, fileName):
    """IO function - queries where to save CSV dataframe"""
    filepath = input("save data to filepath: ")
    saveCSV(filepath, fileName, data)
    
def IOsaveFig(fig, fileName):
    """IO function - queries where to save matplotlib fig"""
    filepath = input("save data to filepath: ")
    saveFigure(filepath, fileName, fig)
    


""" Misc utilities
Assorted general utilities
"""

def strLinesConcatenate(strList, current=""):
    """utility function - concatenates and returns strList with line breaks"""
    if(len(strList)==1):
        return '\n'.join([current, str(strList[0])])
    else:
        return '\n'.join([current, strLinesConcatenate(strList[1:],current=str(strList[0]))])
    
testArray = np.array(["entry 1", 2, "entry 3", True])
print(strLinesConcatenate(testArray))