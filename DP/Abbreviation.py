#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : abcTransDp.py
# @Author: MoonKuma
# @Date  : 2019/5/16
# @Desc  : see the question at https://www.hackerrank.com/challenges/abbr/problem
# The trick is to compare xxxxXXXxxxXXxF,xxxXXXxF is equal to compare xxxxXXXxxxXXx,xxxXXXx
# Caution to compare xxxxXXXXxxxa,xxxxXXXxxXA, is equal to the "or" between xxxxXXXXxxx,xxxxXXXxxX or xxxxXXXXxxx,xxxxXXXxxXA

def is_equal(a,b):
    len_a = len(a)
    len_b = len(b)
    len_a_dp = len_a + 1
    len_b_dp = len_b + 1
    dp_matrix = list()
    for i in range(len_a_dp):
        dp_matrix.append(list())
        for j in range(len_b_dp):
            dp_matrix[i].append(0)

    # problems where len(a) and len(b) are all 0
    dp_matrix[0][0] = 1

    # problems where len(b) is 0 (in this case, all what a left should be lower)
    for i in range(1,len_a_dp,1):
        if a[0:i].islower():
            dp_matrix[i][0] = 1
        else:
            dp_matrix[i][0] = 0

    # problems where len(b) is not 0 (in this case, we break it up into sub-problems)
    for i in range(1,len_a_dp):
        for j in range(1,len_b_dp):
            # i<j means the remain of a is smaller than that of b, this has to be wrong
            if i<j:
                dp_matrix[i][j] = 0
            if i>=j:
                # the remain of a has a upper letter in its end and it is not same with what of B, this won't work
                if a[i-1].isupper() and a[i-1] != b[j-1]:
                    dp_matrix[i][j] = 0

                # the remain of a has an upper letter in its end and it is the same with what of B,
                # this depends on its sub case
                if a[i-1].isupper() and a[i-1] == b[j-1]:
                    dp_matrix[i][j] = dp_matrix[i-1][j-1]

                # the remain of a has a lower letter in its end and it is the same with what of B,
                # this depends on its sub case
                if a[i - 1].islower() and a[i - 1] == b[j - 1]:
                    dp_matrix[i][j] = dp_matrix[i - 1][j - 1]

                if a[i - 1].islower() and a[i - 1] != b[j - 1] and a[i - 1].upper()!=b[j - 1]:
                    dp_matrix[i][j] = dp_matrix[i - 1][j]

                if a[i - 1].islower() and a[i - 1] != b[j - 1] and a[i - 1].upper()==b[j - 1]:
                    dp_matrix[i][j] = dp_matrix[i - 1][j]|dp_matrix[i - 1][j - 1]

    if dp_matrix[len_a][len_b]:
        return 'YES'
    else:
        return 'NO'


files = list(open('JS/test.txt', 'r').readlines())
lent = len(files)
for i in range(0,lent,2):
    a = files[i].strip()
    b = files[i+1].strip()
    print(is_equal(a,b) + '\n')
