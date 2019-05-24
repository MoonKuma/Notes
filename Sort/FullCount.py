#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : FullCount.py
# @Author: MoonKuma
# @Date  : 2019/5/24
# @Desc  : A sort problem see https://www.hackerrank.com/challenges/countingsort4/problem
# Also number is between 0 and 99, which means one could construct a [[],[]....[]] as 100 total position
# use counting sort to sort a list while keeping the order of the strings preserved
# This seems to be an easy implementation and ' '.join do helped a lot

def countSort(arr):
    len_a = len(arr)

    # construct a counting sort
    sort_list = list()
    for i in range(0,100,1):
        new_list = list()
        sort_list.append(new_list)

    # place each pair from data into this sort list
    for i in range(0,len(arr)):
        pair = arr[i]
        pos = int(pair[0])
        value = pair[1]
        if i<len_a/2:
            value = '-'
        sort_list[pos].append(value)

    # print result
    result_list = list()
    for small_list in sort_list:
        if len(small_list)>0:
            str2 = ' '.join(small_list)
            result_list.append(str2)

    print(' '.join(result_list))

    return ' '.join(result_list)


if __name__ == '__main__':

    arr = list()

    file_op = open('TestData/test.txt','r')
    for line in file_op.readlines():
        line = line.strip()
        array = line.split(' ')
        arr.append(array)

    countSort(arr)
