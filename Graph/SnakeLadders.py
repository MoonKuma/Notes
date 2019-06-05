#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : SnakeLadders.py
# @Author: MoonKuma
# @Date  : 2019/6/5
# @Desc  : graph problem : https://www.hackerrank.com/challenges/the-quickest-way-up/problem
# Seems that this could also be solved with Dijkstra

import sys


def quickestWayUp(ladders, snakes):
    """
    This could also be regarded as a breadth first search problem in finding the shortest way
    Distance here could be regarded as the time of rolling the dice
    For example, 21 is connected to [22~27] in the distance of 1 (1 roll of dice)
    For ladders, it means to clean all other connections and set the square (bottom) connected to its top with distance of 0
    And snake is the reversed version of ladder
    :param ladders: list of ladder, eg: [[32,62],[42,68],[12,98]]
    :param snakes: list of snakes, eg: [[95,13],[97,25],[93,37],[79,27],[75,19],[49,47],[67,17]]
    :return: minimum num of rolls
    """

    max_int = sys.maxsize
    # initial graph for current problem
    graph = []
    n_node = 100
    for i in range(0, n_node):
        graph.append([max_int]*n_node)

    for i in range(0,len(graph),1):
        for j in range(i+1,i+7,1):   # as the range of each row
            if j<len(graph):
                graph[i][j] = 1

    Q = list(range(0,len(graph))) # query list

    # load ladders and snakes
    for pairs in ladders:
        graph[pairs[0]-1] = [max_int]*n_node
        graph[pairs[0] - 1][pairs[1] - 1] = 0
    for pairs in snakes:
        graph[pairs[0] - 1] = [max_int] * n_node
        graph[pairs[0] - 1][pairs[1] - 1] = 0

    # now compute the distance array from start point(0)
    dist = graph[0]
    dist[0] = 0
    while Q:
        tmp_min = max_int
        node_min = -1
        for node in range(0,len(dist)):
            if node in Q:
                if dist[node]<tmp_min:
                    node_min = node
                    tmp_min = dist[node]
        if node_min == -1:
            break
        Q.remove(node_min)
        for node2 in range(0,len(graph[node_min])):
            if dist[node_min] + graph[node_min][node2] < dist[node2]:
                dist[node2] = dist[node_min] + graph[node_min][node2]

    # print(dist)
    if dist[n_node-1] == max_int:
        return -1
    else:
        return dist[n_node-1]



ladders = [[32,62],[42,68],[12,98]]
snakes = [[95,13],[97,25],[93,37],[79,27],[75,19],[49,47],[67,17]]
print(quickestWayUp(ladders=ladders,snakes=snakes))