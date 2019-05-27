#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : RadioTransmitters.py
# @Author: MoonKuma
# @Date  : 2019/5/27
# @Desc  : search problem see https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
# Note that all radios has to be built onside of a certain house

k = 2
x_str = '9 5 4 2 6 15 12'.split(' ')
x = list()
for i in x_str:
    x.append(int(i))

def radio_transmitters(x, k):
    count_list = list()
    x_sort = sorted(x)
    for i in range(0, x_sort[len(x_sort)-1]+1):
        count_list.append(0)
    for x_num in x_sort:
        count_list[x_num]+=1
    radio = 0
    index = 1
    max_index = len(count_list) - 1
    while index<=max_index:
        if count_list[index]==0:
            index +=1
            continue
        # backward search to make sure the radio is built on some house
        for j in range(index+k, index-1,-1):
            if j<=max_index and count_list[j]>0:
                break
        index = j + k + 1
        radio +=1


print(radio_transmitters(x,k))