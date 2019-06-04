#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : JourneyToMoon.py
# @Author: MoonKuma
# @Date  : 2019/6/3
# @Desc  : see: https://www.hackerrank.com/challenges/journey-to-the-moon/problem
# This seems to be another find and union problem


def journeyToMoon(n, astronaut):
    """
    Using a find and union model to solve this pair-up question
    Union those pairs, find the number/size of trees then match up
    :param n: number of astronauts
    :param astronaut: astronaut list (the list to union)
    :return: number of pairs
    """

    # the implementation of compressed find-union class

    id_list = list(range(0,n,1))
    sz_list = []
    for _ in id_list:
        sz_list.append(1)

    # compressed find
    def root(i):
        while i!=id_list[i]:
            # compressed here by point it to its grandparent
            id_list[i] = id_list[id_list[i]]
            i = id_list[i]
        return i

    # fast & balanced union
    def union(p,q):
        p_root = root(p)
        q_root = root(q)
        if p_root == q_root:
            return
        # compare size then union
        # add the smaller tree to the larger one to save computation in rewrite in root(i)
        if sz_list[p_root] >= sz_list[q_root]:
            id_list[q_root] = p_root
            sz_list[p_root] += sz_list[q_root]
        else:
            id_list[p_root] = q_root
            sz_list[q_root] += sz_list[p_root]

    # now solve the task
    # union countries
    for pairs in astronaut:
        union(pairs[0],pairs[1])
    # count roots
    roots = set()
    for i in id_list:
        roots.add(root(i))
    # figure size of each root
    # those who has size of 1 is separated for fast computation
    root_size_more = list()
    root_size_1 = 0
    for i in roots:
        sz = sz_list[i]
        if sz==1:
            root_size_1 += 1
        else:
            root_size_more.append(sz_list[i])
    # compute pairs in 2 iterations for those with size>=2
    sum_pairs = 0
    for i in range(0,len(root_size_more)):
        for j in range(i+1,len(root_size_more)):
            sum_pairs += root_size_more[i] * root_size_more[j]

    # those with size of 1, this is a simple computation
    sum_pairs += (n-root_size_1)*root_size_1 + int((root_size_1*(root_size_1-1))/2)
    return sum_pairs


# test
test_list = [[0,1],[2,3],[0,4]]
test_n = 5

print(journeyToMoon(n=test_n,astronaut=test_list))