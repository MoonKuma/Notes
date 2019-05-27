#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Pairs.py
# @Author: MoonKuma
# @Date  : 2019/5/27
# @Desc  : Search problem see https://www.hackerrank.com/challenges/pairs/problem
# Well, this is such a easy problem which doesn't worse that many points

k = 2
x_str = '1 5 3 4 2'.split(' ')
x = list()
for i in x_str:
    x.append(int(i))

# My solution
def pairs(k, arr):
    x_sort = sorted(arr)
    pairs = 0
    num_set = set()
    for num in x_sort:
        num_set.add(num)
        if num-k in num_set:
            pairs += 1
    return pairs

# Someone offer the one line solution
def pairs_2(k, arr):
    return len(set(arr) & set(x + k for x in arr))

# Also, it's possible in doing this inside a list known as binary approach

def pairs_3(k, arr):
    x_sort = sorted(arr)
    pairs = 0
    i = 0
    j = 0
    max_len = len(x_sort) - 1
    while i<= max_len and j<=max_len:
        diff = x_sort[j] - x_sort[i]
        if diff == k:
            i += 1
            j += 1
            pairs +=1
        if diff<k:
            j +=1
        if diff>k:
            i +=1
    return pairs


print(pairs_3(k,x))