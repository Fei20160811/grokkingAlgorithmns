#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:19:09 2023

@author: ml
"""
def quick_sort(data):
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        less = [item for item in data if item < pivot]
        greater = [item for item in data if item > pivot]
        
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
    
print(quick_sort([10, 5, 2, 3, 7]))