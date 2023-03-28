#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:30:25 2023

@author: ml
"""
def factorail(x):
    #base case
    if x == 1:
        return 1
    #recursive case
    else:
        return x * factorail(x-1)
    
    
print(factorail(3))