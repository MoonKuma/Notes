#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ConnectedCell.py
# @Author: MoonKuma
# @Date  : 2019/5/27
# @Desc  : Another search problem at https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
# This passed test, but it's ugly to search all 8 directions
# Notion, there is another way (Union-Find) of solving this,
# https://www.coursera.org/learn/algorithms-part1/supplement/bcelg/lecture-slides
# Take some time to watch that later


def connectedCell(matrix):

    n_row = len(matrix)
    n_col = len(matrix[0])
    # checked is used to remember those area that has been searched
    # one can also set all those that has been searched into 0, which will change the matrix though
    checked = set()

    max_area = 0

    def pair_key(r,c):
        return str(r) + '|' + str(c)

    def get_area(r,c):
        if pair_key(r,c) in checked:
            return 0
        checked.add(pair_key(r,c))
        # the wall
        if r<0 or r>=n_row or c<0 or c>=n_col:
            return 0
        if matrix[r][c] == 0:
            return 0
        if matrix[r][c] == 1:
            # all 8 directions are necessary in this case
            return 1 + get_area(r+1,c) + get_area(r,c+1)\
                   + get_area(r-1,c) + get_area(r,c-1) \
                   + get_area(r+1,c+1) + get_area(r+1,c-1)\
                   + get_area(r-1,c+1) + get_area(r-1,c-1)

    for row in range(0, n_row):
        for column in range(0, n_col):
            if pair_key(row, column) in checked:
                continue
            local_max = get_area(row, column)
            if local_max > max_area:
                max_area = local_max

    return max_area


if __name__ == '__main__':

    matrix = []

    data = open('TestData/test.txt', 'r')

    for line in data.readlines():
        matrix.append(list(map(int, line.strip().split(' '))))

    result = connectedCell(matrix)
    print(result)

