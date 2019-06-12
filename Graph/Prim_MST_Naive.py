#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Prim_MST.py
# @Author: MoonKuma
# @Date  : 2019/6/6
# @Desc  : Prim's method in making a minimum-cost spanning tree: https://www.hackerrank.com/challenges/primsmstsub/problem
# I really should watch the official tutorial video sometime instead of writing by imagination
# The current prim's method is not recommended for its complexity O(n^2), yet still this could work as a start to MST


import sys

def prims(n, edges, start):
    """
    Prim's method in find the MST (minimum-cost spanning tree)
    The start doesn't matter though
    The trick is some kind of greedy method
    As :
    1. find a random start point (the start point doesn't matter because all nodes need to be connected)
    2. make two set as the visited set V = [s] and search set S,
    3. find the short edges between current V and S, and the node in S into V, record its weight
    4. repeat step 3 util S become empty
    The step 3 is valid because, if there is a current shortest path but that path is not selected to reach this node,
    then we could add this edge in to the final graph (make it some kind of cycle) and then remove one of the longer
    edges and get a better answer.
    :param n: an integer that represents the number of nodes in the graph
    :param edges: list of edges, as the two node and its weight [[1,5,100],[1,7,200]], for the current problem,
                  the edge is undirected and there may be multiple edges between two nodes.
    :param start: a picked start point
    :return: minimum sum of weights
    """

    max_int = 100000




    graph = []
    for i in range(0, n):
        """
        initial the graph, the list[list] may cause some time out error for the cost in searching meaningless maximum values
        we could change it into a map/dict which only maintain the valid connections
        """
        graph.append(dict())

    # load edges
    for pairs in edges:
        node1 = pairs[0] -1
        node2 = pairs[1] -1
        weight = pairs[2]
        if graph[node1].setdefault(node2,max_int)>weight:
            graph[node1][node2] = weight
        if graph[node2].setdefault(node1,max_int)>weight:
            graph[node2][node1] = weight

    # Prim's method
    s = start - 1
    V = [s] # visited list
    """
    you don't need this S.
    
    """
    S = list(range(0,n)) # search list
    S.remove(s)


    weight_sum = 0

    while len(V)<n:
        min_node = -1
        tmp_min = max_int
        for node1 in V:
            """
            There is a trick here in deciding which to iterate and which to test, 
            for the set 'graph[node1].keys()' as the number of edges in node1 will be relatively smaller 
            than the search list S or visited list V.
            if you try:
            for node2 in S:
                if node2 in graph[node1].keys():
                    ...
            Then you will get some timeout error. LOL
            """
            """
            Such modification helps pass one Time Out problem.
            There must be some other techniques here...
            """

            for node2 in graph[node1].keys():
                if node2 not in V:
                    if graph[node1][node2] < tmp_min:
                        min_node = node2
                        tmp_min = graph[node1][node2]
        if min_node == -1:
            break
        V.append(min_node)
        # S.remove(min_node)
        weight_sum += tmp_min

    return weight_sum

# test
test_edges = [[1,2,3],[1,3,4],[4,2,6],[5,2,2],[2,3,5],[3,5,7]]
test_start = 1
n =5
print(prims(n=n, edges=test_edges,start=test_start))


# # test the time-out cases
# import time
#
# data_file = open('TestData/test3.txt', 'r')
# edges = []
# for line in data_file.readlines():
#     line = line.strip()
#     edges.append(list(map(int, line.split(' '))))
#
# m = len(edges)
# print(m)
# n = 1000
# t0 = time.time()
# print(prims(n, edges, 2))
# print(time.time()-t0)
#


