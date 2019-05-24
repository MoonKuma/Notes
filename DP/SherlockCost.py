#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : SherlockCost.py
# @Author: MoonKuma
# @Date  : 2019/5/22
# @Desc  : https://www.hackerrank.com/challenges/sherlock-and-cost/problem
# The trick is there is meaningless for select something in the middle,
# it's either the largest num in range or the smallest
# Besides, the next choice won't influence the best 2 solutions before it

import math

test_list = [10, 1, 10, 1, 10]

def cost(B):
    # initial dp_matrix
    dp_matrix = list()
    for i in range(0, 2):
        new_list = list()
        for k in range(0, len(B), 1):
            new_list.append(0)
        dp_matrix.append(new_list)

    # compute result of each step
    for i in range(1,len(B),1):
        dp_matrix[0][i] = max(dp_matrix[0][i-1],dp_matrix[1][i-1]+abs(B[i-1]-1))
        dp_matrix[1][i] = max(dp_matrix[0][i - 1]+abs(B[i]-1), dp_matrix[1][i - 1] + abs(B[i - 1] - B[i]))

    # return the solution which get best total score
    return max(dp_matrix[0][len(B)-1], dp_matrix[1][len(B)-1])

print(cost(test_list))

