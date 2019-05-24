#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LilyHomework.py
# @Author: MoonKuma
# @Date  : 2019/5/23
# @Desc  : A sort problem from https://www.hackerrank.com/challenges/lilys-homework/problem
# First trick is there are actually two possible answers for certain given list
# [1,5,4,2,3] => [5,4,3,2,1], [1,5,4,2,3] => [1,2,3,4,5]
# !!! The second trick is to load the list (value and its position) into a map to save the cost for searching index
import time
test_arr = [2,5,3,1]

def lilysHomework(arr):
    # need to copy for the manipulation modified array a
    # although there is no need for deep copy since the list is full of integer
    arr_copy = arr.copy()

    ans1 = sorted(arr)
    ans2 = sorted(arr, reverse=True)

    # here is the wrong way of getting index, neither iterable works here (time out error, a test with 100000 will cost 228s)
    def get_index(a_list, value):
        return a_list.index(value)

    # this is the correct version, as time cost will be narrowed into 0.2s
    def get_index_map(a_list_map,value):
        return a_list_map[value]

    def count_rank(target,answer):
        n = 0
        target_map = dict()
        for i in range(0,len(target)):
            target_map[target[i]] = i

        i = 0
        for j in range(0,len(answer)):
            if answer[j] == target[i]:
                i+=1
                continue
            else:
                pos = get_index_map(target_map,answer[j])
                tmp = target[i]
                target[i] = answer[j]
                target[pos] = tmp
                target_map[tmp] = pos
                n+=1
                i+=1
        return n

    return min(count_rank(arr,ans1),count_rank(arr_copy,ans2))


file_op = open('TestData/test.txt', 'r').readlines()
a = list()
for line in file_op:
    line = line.strip()
    array = line.split(' ')
    for k in array:
        a.append(int(k))
    t0 = time.time()
    print(lilysHomework(a))
    print('time cost:',time.time()-t0)
