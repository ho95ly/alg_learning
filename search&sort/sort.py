# -*- coding: utf-8 -*-
__author__ = 'h0ly95'

import numpy as np


def merge(a, b):
    c = list()
    h = 0
    j = 0
    len_b = len(b)
    len_a = len(a)
    while h < len_b and j < len_a:
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len_a:
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def mergeSort(list):
    list_len = len(list)
    if list_len <= 1:
        return list
    middle_cursor = int(list_len/2)
    left_list = mergeSort(list[:middle_cursor])
    right_list = mergeSort(list[middle_cursor:])
    return merge(left_list, right_list)


if __name__ == '__main__':
    k = [4, 8, 3, 7, 1, 5, 6]
    p = mergeSort(k)
    print(p)
