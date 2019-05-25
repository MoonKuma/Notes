#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : FraudulentActivity.py
# @Author: MoonKuma
# @Date  : 2019/5/24
# @Desc  : Another sort problem, see https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
# There is a blunt way in doing those tiny sort work, yet this is not economical and may cause time out error
# The real trick is conceived insides its constraints as
# 1<= n <= 2*10E5
# 1<= d <= n
# 0< expenditure[i] < 200
# Because the value inside expenditure is limited, counting sort is applicable now

import time

def activityNotifications(expenditure, d):

    # well, let's try the stupid way first (for test with len(expenditure)=200000 and d=10000,
    # this mean to call sort for like 2*10E9 times)
    def get_answer(expenditure, d):
        d_list = list()
        notice = 0
        for i in range(0,len(expenditure)):
            if len(d_list)<d:
                d_list.append(expenditure[i])
                continue
            else:
                d_sort = sorted(d_list)
                if d%2==0:
                    double_mid = d_sort[int(d/2)] + d_sort[int(d/2-1)]
                else:
                    double_mid = d_sort[int((d-1) / 2)] * 2
                if expenditure[i]>= double_mid:
                    notice +=1
                d_list.pop(0)
                d_list.append(expenditure[i])
        return notice

    # now it's time we try some clever way (some kind of counting sort)
    def get_answer_correct(expenditure, d):
        count_sort = list()
        for i in range(0,201,1):
            count_sort.append(0)

        # first d times
        for i in range(0,d,1):
            count_sort[expenditure[i]] +=1

        # find the rank k value
        def find_rank(count_sort, k ):
            now = 0
            for i in range(0,len(count_sort)):
                now += count_sort[i]
                if now>=k:
                    return [i,now-k]

        # compute the rest of expenditure
        if d%2==1:
            [target, rank] = find_rank(count_sort,int((d+1)/2))
            threshold = target*2
            notice = 0
            for i in range(d,len(expenditure),1):
                value = expenditure[i]
                if value>=threshold:
                    notice +=1
                count_sort[expenditure[i-d]] = count_sort[expenditure[i-d]]-1
                count_sort[expenditure[i]] += 1
                if (expenditure[i-d]<target and expenditure[i]<target) or (expenditure[i-d]>target and expenditure[i]>target) or (expenditure[i-d]==target and expenditure[i]==target):
                    continue
                else:
                    [target, rank] = find_rank(count_sort, int((d + 1) / 2))
                    threshold = target * 2
        else:
            [target0, rank0] = find_rank(count_sort,int(d/2))
            [target1, rank1] = find_rank(count_sort, int(d / 2)+1)
            threshold = target0 + target1
            notice = 0
            for i in range(d,len(expenditure),1):
                value = expenditure[i]
                if value>=threshold:
                    notice +=1
                count_sort[expenditure[i-d]] = count_sort[expenditure[i-d]]-1
                count_sort[expenditure[i]] += 1
                if (expenditure[i-d]<target0 and expenditure[i]<target0) or (expenditure[i-d]>target1 and expenditure[i]>target1) or (expenditure[i-d]==target0 and expenditure[i]==target0) or (expenditure[i-d]==target1 and expenditure[i]==target1):
                    continue
                else:
                    [target0, rank0] = find_rank(count_sort, int(d / 2))
                    [target1, rank1] = find_rank(count_sort, int(d / 2) + 1)
                    threshold = target0 + target1
        return notice

    return get_answer_correct(expenditure=expenditure,d=d)









if __name__ == '__main__':

    arr = list()

    file_op = open('TestData/test2.txt','r')

    line1 = file_op.readline()
    line1 = line1.strip()
    array = line1.split(' ')
    d = int(array[1])
    line2 = file_op.readline()
    line2 = line2.strip()
    array = line2.split(' ')
    expenditure = list()
    for i in array:
        expenditure.append(int(i))

    t0 = time.time()
    print(activityNotifications(expenditure=expenditure,d=d))
    print('Time Cost:',time.time()-t0,'\s')
