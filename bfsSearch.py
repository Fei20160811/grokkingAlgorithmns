#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:13:41 2023

@author: ml
"""

from collections import deque


def find_orange_seller(name):
    return name[-1] == "m"


def bfs_search(name):
    #產生deque物件
    find_deque = deque()
    #將第一層關係人加入佇列
    find_deque += graph[name]
    #紀錄已經查詢過的人
    searched = []
    
    while find_deque:
        #取出佇列中的第一個人
        people = find_deque.popleft()
        #查詢此人是否已查詢過
        if people not in searched:
            #查詢是否為橘子銷售商
            if find_orange_seller(people):
                return people + "為橘子銷售商"
            else:
                #將查詢者的下一層關係人加入佇列
                #將目前查詢者的資料加入以查詢列表
                find_deque += graph[people]
                searched.append(people)
    return "朋友圈中沒有橘子銷售員"



graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(bfs_search("you"))