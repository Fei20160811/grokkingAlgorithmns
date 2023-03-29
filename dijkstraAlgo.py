#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:26:08 2023

@author: ml
"""

searched = []

def find_lowest_node_cost(costs):
    lowest_value = float("inf")
    lowest_node = None
    
    for cost in costs:
        if costs[cost] < lowest_value and cost not in searched:
            lowest_value = lowest_value
            lowest_node = cost
    return lowest_node

def dijkstra_algo():
    #圖形雜湊表
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    graph["fin"] = {}

    #成本雜湊表
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    #float("inf") => 無窮大
    costs["fin"] = float("inf")

    #父節點雜湊表
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None
    
    
    #從成本最小的點開始處理
    node = find_lowest_node_cost(costs)

    while node:
        
        #取出該節點成本
        cost = costs[node]
        #取出該節點相鄰點
        neighbor = graph[node]

        #處理此節點所有的相鄰節點
        for item in neighbor.keys():
            new_cost = cost + neighbor[item]
            #如果通過此節點到達相鄰節點數值小於原先成本表數值，則更新此節點的成本資料與父點資料
            if new_cost < costs[item]:
                costs[item] = new_cost
                parents[item] = node
        #註記處理過的節點
        searched.append(node)
        #找下一個成本最小的點
        node = find_lowest_node_cost(costs)
    
    return costs


print(dijkstra_algo())
