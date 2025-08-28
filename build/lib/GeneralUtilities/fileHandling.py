#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 12:06:55 2025

@author: nayandusoruth
"""

import os
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
    
    file = open((filename + ".txt"), "a")
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
    fig.savefig(fileName, dpi=300, bbox_inches='tight')
    
    # go back to original directory
    os.chdir(curDir)
