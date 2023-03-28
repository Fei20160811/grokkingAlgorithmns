#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:55:47 2023

@author: ml
"""
def find_largest_num(data):
    if len(data) == 1:
        return data[0]
    else:
        return data[0] if data[0] > find_largest_num(data[1:]) else find_largest_num(data[1:])
          

print(find_largest_num([6]))
print(find_largest_num([20,8,6,45,12,3]))
    