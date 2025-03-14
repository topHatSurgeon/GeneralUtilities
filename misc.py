#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 12:12:09 2025

@author: nayandusoruth
"""
import numpy as np



""" Misc utilities
Assorted general utilities
"""

def strLinesConcatenate(strList, current=""):
    """utility function - concatenates and returns strList with line breaks"""
    if(len(strList)==1):
        return '\n'.join([current, str(strList[0])])
    else:
        return '\n'.join([current, strLinesConcatenate(strList[1:],current=str(strList[0]))])