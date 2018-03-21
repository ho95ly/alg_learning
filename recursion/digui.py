# -*- coding: utf-8 -*-
__author__ = 'h0ly95'


def recursion_jiecheng(n):
    if n == 0:
        return 1
    return n*recursion_jiecheng(n-1)


def fibonacci(n):
    if n<=1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


def devide_int(n, m):
    if n < 0 or m < 0:
        return 0
    if n == 1 or m == 1:
        return 1
    if n < m:
        return devide_int(n, n)
    if n == m:
        return devide_int(n, m-1)+1
    return devide_int(n, m-1)+devide_int(n-m, m)


def hanoi(n, a, b, c):
    if n == 1:
        print(a, '->', c)
        return 0
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)




if __name__ == '__main__':
    a = hanoi(3, 'a', 'b', 'c')
    print(a)