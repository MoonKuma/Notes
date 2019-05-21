#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : CoinChange.py
# @Author: MoonKuma
# @Date  : 2019/5/17
# @Desc  : https://www.hackerrank.com/challenges/coin-change/problem

# The trick is f(10) = f(10-6) + f(10-5) + f(10-3) + f(10-2)
# Caution, when you use f(10-3), it means the largest of its sub-task should be no larger than 3
# i.e. It can't be like f(10) = f(10-3) = f(8-5), for such way is computed through f(10) = f(10-5) = f(5-3)
# Or to say, you can only moving left or moving left+up. No left+down.

# n = 10
# c = [2,5,3,6]

def getWays(n, c):

    c.sort()
    dp_list = list()
    for i in range(0, len(c), 1):
        min_list = list()
        min_list.append(1)
        for i in range(1, n + 1, 1):
            min_list.append(0)
        dp_list.append(min_list)

    if c[0] > n:
        return 0

    for i in range(1, n + 1):
        for j in range(0, len(c)):
            num = 0
            for s_j in range(0, j + 1):
                if i >= c[s_j]:
                    num += dp_list[s_j][i - c[s_j]]
            dp_list[j][i] = num
    return dp_list[len(c) - 1][n]

#test
c = [1,2,3]
n = 4
print(getWays(n, c))
