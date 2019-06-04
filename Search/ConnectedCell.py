#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ConnectedCell.py
# @Author: MoonKuma
# @Date  : 2019/5/27
# @Desc  : Another search problem at https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
# This passed test, but it's ugly to search all 8 directions
# Notion, there is another way (Union-Find) of solving this,
# https://www.coursera.org/learn/algorithms-part1/supplement/bcelg/lecture-slides
# I tried implement one in fast find union model later


def fast_find_union(matrix):
    """
    Using find union model to solve the problem
    This implementation avoids the recursive method. Besides, it is believed to be super efficient for larger problems
    :param matrix: input matrix
    :return: num of connected area
    """
    n_row = len(matrix)
    n_col = len(matrix[0])
    total_size = n_row * n_col
    id_list = list()
    sz_list = list()

    # initialize
    # each node is its own root
    # each tree has the size of 1
    for i in range(0,total_size):
        id_list.append(i)
        sz_list.append(1)

    # define find function
    def root(i):
        while i!=id_list[i]:
            # Path compression, this is not necessary, but it helps flatting the structure
            id_list[i] = id_list[id_list[i]]
            # original find func
            i = id_list[i]
        return i

    # define union function
    def union(p, q):
        i = root(p)
        j = root(q)
        if i==j:
            return
        # the size list help to balance each tree (the smaller branch get attached to the larger )
        if sz_list[i]<sz_list[j]:
            id_list[i] = j
            sz_list[j] += sz_list[i]
        else:
            id_list[j] = i
            sz_list[i] += sz_list[j]

    # define is_connected function
    def is_connected(p, q):
        return root(p) == root(q)

    # this is the service function to solve current problem
    def main(matrix):
        for row in range(0,n_row):
            for col in range(0,n_col):
                index = row*n_col + col
                value = matrix[row][col]
                if value ==1:
                    # when scanned in this way( from up-left to right-down), you only need to watch out four direction
                    if row+1<n_row and matrix[row+1][col]==1:
                        union(index, (row+1)*n_col + col)
                    if col+1<n_col and matrix[row][col+1]==1:
                        union(index, row * n_col + col+1)
                    if row+1<n_row and col+1<n_col and matrix[row+1][col+1]==1:
                        union(index, (row+1) * n_col + col + 1)
                    if row+1<n_row and col-1>=0 and matrix[row+1][col-1]==1:
                        union(index, (row+1) * n_col + col - 1)
        # after union all of them, the max area is already kept inside the size_list
        # we only need to find the largest value in size list
        n_max = 0
        for item in sz_list:
            if item>n_max:
                n_max=item
        return n_max


    return main(matrix)



def connectedCell(matrix):
    """
    This is the original recursive implementation
    :param matrix: input n*m matrix
    :return: the largest area
    """
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

    # result = connectedCell(matrix)
    result = fast_find_union(matrix)
    print(result)



