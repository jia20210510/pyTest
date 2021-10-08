#!/usr/bin/env python   
# _*_ coding:utf-8 _*_
"""
@version: python3.8
@project:pyTest
@file:   algorithm.py
@date:   2021/10/8 15:30
@Author: jia
@Desc:
"""
import time
start = time.perf_counter()


# 冒泡排序 时间复杂度（n^2）
def bubble_sort(list_num):
    if len(list_num) < 1:
        return list_num
    for i in range(len(list_num)-1):
        for j in range(len(list_num)-1-i):
            if list_num[j] < list_num[j+1]:
                list_num[j], list_num[j+1] = list_num[j+1], list_num[j]
    print(list_num)


# 快速排序 时间复杂度（nlogn）
def quick_sort(list_num, left, right):
    if left >= right:
        return list_num
    pivot = list_num[left]
    low = left
    high = right
    while left < right:
        while left < right and list_num[right] > pivot:
            right -= 1
            # print('right is ', right)
        # print('right:', right)
        list_num[left] = list_num[right]
        while left < right and list_num[left] < pivot:
            left += 1
        list_num[right] = list_num[left]
        list_num[left] = pivot
        quick_sort(list_num, low, left-1)
        quick_sort(list_num, right+1, high)
    print(list_num)
    print('Runtime is %s' % (end-start))
    return list_num


end = time.perf_counter()
if __name__ == '__main__':
    # bubble_sort([0, 3, 1, 99, 80])
    arr = [30, 10, 20, 50, 40, 60]
    quick_sort(arr, 0, len(arr)-1)