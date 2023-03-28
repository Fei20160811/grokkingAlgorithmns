#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:41:28 2023

@author: ml
"""

def find_smallest_index(data):
    smallest_index = 0
    smallest_value = data[0]
    
    for i in range(1, len(data)):
        if data[i] < smallest_value:
            smallest_index = i
            smallest_value = data[i]
    
    return smallest_index

def selection_sort(data):
    new_arr = []
    
    for i in range(len(data)):
        #每次查找一個最小值
        smallest_index = find_smallest_index(data)
        #將該值從原本的data中取出，加入新的arr中
        new_arr.append(data.pop(smallest_index))
        
    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))