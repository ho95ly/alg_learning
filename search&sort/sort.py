# -*- coding: utf-8 -*-
__author__ = 'h0ly95'

import numpy as np
import time


def bubbleSort(arr):
    length = len(arr)
    for j in range(length):
        for i in range(length-1-j):
            if arr[i] > arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
    return arr


def bubbleSort2(arr):
    length = len(arr)
    j = length-1
    while j > 0:
        pos = 0
        for i in range(j):
            if arr[i] > arr[i + 1]:
                pos = i
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
        j = pos

    return arr


def bubbleSort3(arr):
    length = len(arr)
    low = 0
    high = length-1
    while low < high:
        for i in range(low, high):
            if arr[i] > arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
        high = high - 1
        for i in range(high, low, -1):
            if arr[i] < arr[i - 1]:
                tmp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = tmp
        low = low + 1

    return arr


def selectionSort(arr):
    length = len(arr)
    for i in range(length-1):
        minIndex = i
        for j in range(i+1, length):
            if arr[j] < arr[minIndex]:
                minIndex = j
        tmp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = tmp
    return arr


def insertionSort(arr):
    length = len(arr)
    for i in range(length):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr


def binaryInsertionSort(arr):
    length = len(arr)
    for i in range(length):
        key = arr[i]
        left = 0
        right = i-1
        while left < right:
            middle = int((left + right)/2)
            if key < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1
        for j in range(i-1, left-1, -1):
            arr[j + 1] = arr[j]
        arr[left] = key
    return arr


def shellSort(arr, delta_list):
    length = len(arr)
    for gap in delta_list:
        for i in range(gap, length):
            tmp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > tmp:
                arr[j+gap] = arr[j]
                j = j - gap
            arr[j+gap] = tmp
    return arr


def quickSort(arr, left, right):
    if left < right:
        x = arr[right]
        i = left - 1
        for j in range(left, right+1):
            if arr[j] <= x:
                i = i+1
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
        quickSort(arr, left, i-1)
        quickSort(arr, i+1, right)
    return arr

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
    a = np.random.rand(15)
    start = time.time()
    b = quickSort(a, 0, len(a)-1)
    end = time.time()
    print(str(end - start))
    #print(aa)
    print(b)
