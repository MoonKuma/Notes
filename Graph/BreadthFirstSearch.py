#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : BreadthFirstSearch.py
# @Author: MoonKuma
# @Date  : 2019/6/3
# @Desc  : https://www.hackerrank.com/challenges/bfsshortreach/problem
# A classic problem, let's try solve it first
# Also, watch the video :https://www.coursera.org/learn/algorithms-part2/lecture/DjaET/breadth-first-search


import sys


def bfs(n, m, edges, s):
    """
    Standard breadth-first-search method (the Dijkstra)
    Note in solving current problem, the starts and edges are subtracted by 1
    Also, this is a undirected map
    :param n: number of nodes
    :param m: number of edges, not useful here
    :param edges: array of edges as [node1, node2], the official version should be [node1,node1,weight],
                 for this problem, all weights are set to a constant
    :param s: node of start
    :return: a list showing the distance between start point and each nodes
    """

    s = s-1
    max_int = sys.maxsize
    graph = list()

    for i in range(0, n):
        graph.append([max_int]*n)

    # load edge and weights (for this problem which starts from 1 instead of 0, edge index need to be subtracted by 1)
    for edge in edges:
        graph[edge[0]-1][edge[1]-1] = 6
        graph[edge[1]-1][edge[0]-1] = 6

    # Dijkstra
    dist = []
    for i in graph[s]:
        dist.append(i)
    dist[s] = 0

    #  S & Q
    S = [] # visited list, why we need this?
    Q = list(range(0,n))

    while Q:
        # to find the node of minimum distance in Q
        min_tmp = max_int
        min_node = -1
        for node, d in enumerate(dist):
            if node in Q:
                if d < min_tmp:
                    min_tmp = d
                    min_node = node

        # non of them connected
        if min_node == -1:
            break
        # add it into the visited list ( not necessary here, just by convention)
        S.append(min_node)
        # remove it from query list, note the value in Q is the index of graph
        Q.remove(min_node)
        # refresh the dist with standing at the position u
        for v, d in enumerate(graph[min_node]):
            if dist[v] > dist[min_node] + d:
                dist[v] = dist[min_node] + d

    # modify to suit the standard return result
    for i in range(0,len(dist)):
        if dist[i] == max_int:
            dist[i] = -1
    dist.remove(0)
    return dist



n = 4
m = 2
edges = [[1,2],[1,3]]
s = 1

print(bfs(n, m, edges, s))
