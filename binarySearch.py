#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:18:47 2023

@author: ml
"""
def binary_search(data, item):
    
    #持續追蹤要搜尋的list元素    
    low = 0
    high = len(data) - 1
    
    #還沒縮小範圍到只剩一個元素時
    while low <= high:
        #檢查中間的元素
        middle = (low + high) // 2
        guess = data[middle]
        
        #base case
        #找到想找的元素
        if guess == item:
            return middle
        
        #recursive case
        #如果猜測的值比較小，將low的index改為目前的中間值所屬序號往數值大的方向＋1
        if guess < item:
            low = middle + 1
        #如果猜測的值比較大，將hight的index改為目前的中間值所屬序號往數值小的方向-1
        else:
            high = middle - 1
    else:
        #想找的元素不存在
        return None
    
    
#data需先排序過，才能使用二元搜尋
my_list = [1, 3, 5, 7, 9]
    
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))


    
    