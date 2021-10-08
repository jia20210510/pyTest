# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: pyTest
@File: debug.PY
@Date: 2021/6/21 21:29
@Author: jia
@Description:
"""

import copy
import time
start = time.perf_counter()


def copy_test():
    ddict = {'1': 1, '2': [3, 4]}
    copy1 = ddict.copy()
    copy2 = copy.deepcopy(ddict)
    copy3 = copy.copy(ddict)
    ddict['2'][0] = 5
    print('ddct%s,copy3:%s' % (ddict, copy3))


def copy_list():
    list_num = [[1, 2], 'b', 1, 2, 3]
    shallow_copy = copy.copy(list_num)
    deep_copy = copy.deepcopy(list_num)
    list_num[0][0] = 5
    print('list_num %s, shallow_copy: %s, deep_copy: %s' % (list_num, shallow_copy, deep_copy))


def reverse_char():
    # long_char = ['a', 'b', 'c', 'd']
    # long_char.reverse()
    # new_char = long_char[::-1]
    # print(long_char)
    # print(new_char)

    char = 'abcd'
    b = char[::-1]
    c = ','.join(b)
    print(c)


def end_str():
    str = 'i love python.txt'
    str1 = str.endswith('.txt')
    str2 = str.endswith('on', 5, 13)
    str3 = str[0:1]
    print('str1:%s, str2:%s, str3 %s' % (str1, str2, str3))


def split_str():
    list_num = ['a', 'b', 'c', 'd']
    print(list_num[10:])


def math_calculate(a):
    print(a % 12)


def bubble_sort():
    arr = [2, 7, 1, 8, 0, 99]
    for i in range(len(arr)-1):
        # print(list(range(len(arr)-1)))
        for j in range(len(arr)-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print('i:', i)
            print('j:', j)
            print(arr)
    print('runtime:%s seconds' % (end-start))


end = time.perf_counter()
if __name__ == '__main__':
    # copy_test()
    # copy_list()
    # reverse_char()
    # end_str()
    # split_str()
    # math_calculate(2)
    bubble_sort()