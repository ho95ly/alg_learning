# -*- coding: utf-8 -*-
__author__ = 'h0ly95'
import numpy as np


def baniarySearch(num_seq, num):

    len_seq = len(num_seq)
    left_cursor = 0
    right_cursor = len_seq-1
    while left_cursor <= right_cursor:
        middle_cursor = int((left_cursor+right_cursor)/2)

        if num_seq[middle_cursor] == num:
            print('done')
            return middle_cursor
        elif num > num_seq[middle_cursor]:
            print('l')

            left_cursor = middle_cursor + 1
        else:
            print('r')
            right_cursor = middle_cursor - 1
    return False


if __name__ == '__main__':
    a = np.arange(12)
    b = 4
    c = baniarySearch(a, b)

