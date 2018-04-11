# -*- coding: utf-8 -*-
__author__ = 'h0ly95'
import numpy as np


def SequenceSearch(arr, num):
    length = len(arr)
    pos = []
    for i in range(length):
        if arr[i] == num:
            pos.append(i)
    return pos


def binarySearch(num_seq, num):  # element must be sorted.

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


def binarySearch2(arr, num, left_cursor, right_cursor):
    if left_cursor > right_cursor:
        return -1
    middle_cursor = int((left_cursor+right_cursor)/2)
    if a[middle_cursor] == num:
        return middle_cursor
    elif a[middle_cursor] < num:
        return binarySearch2(arr, num, middle_cursor+1, right_cursor)
    elif a[middle_cursor] > num:
        return binarySearch2(arr, num, left_cursor, middle_cursor-1)


def insertionSearch(arr, num, left_cursor, right_cursor):
    if left_cursor > right_cursor:
        return -1
    middle_cursor = int(left_cursor+(num-arr[left_cursor])/(arr[right_cursor]-arr[left_cursor])
                        * (right_cursor-left_cursor))
    if a[middle_cursor] == num:
        return middle_cursor
    elif a[middle_cursor] < num:
        return binarySearch2(arr, num, middle_cursor + 1, right_cursor)
    elif a[middle_cursor] > num:
        return binarySearch2(arr, num, left_cursor, middle_cursor - 1)


def Fibonacci(len=20):

    F = np.zeros(20)
    F[0] = 0
    F[1] = 1
    for i in range(2, len):
        F[i] = F[i-1] + F[i-2]

    return F


def FibonacciSearch(arr, num):
    length = len(arr)
    left_cursor = 0
    right_cursor = length-1
    F = Fibonacci()
    k = 0
    while length > F[k]:
        k = k+1
    tmp_arr = np.zeros(F[k]-1)
    tmp_arr[0:length] = arr

    while left_cursor <= right_cursor:
        middle_cursor = left_cursor+F[k-1]-1
        if num < tmp_arr[middle_cursor]:
            right_cursor = middle_cursor - 1
            k = k-1
        elif num > tmp_arr[middle_cursor]:
            left_cursor = middle_cursor + 1
            k = k-2
        else:
            if middle_cursor < length:
                return middle_cursor
            else:
                return length-1
    return False



if __name__ == '__main__':
    pass

