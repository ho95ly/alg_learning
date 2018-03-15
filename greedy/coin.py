# -*- coding: utf-8 -*-
__author__ = 'h0ly95'

'''
找零钱问题：假设只有 1 分、 2 分、五分、 1 角、二角、 五角、 1元的硬币。
在超市结账 时，如果 需要找零钱， 收银员希望将最少的硬币数找给顾客。那么，给定 需要找的零钱数目，如何求得最少的硬币数呢？
'''


def give_change(coin_list, price, give_money):
    coin_list_s = sorted(coin_list)
    coin_list_sr = list(reversed(coin_list_s))
    exsist_money = give_money - price
    coin_num = list()
    coin = coin_list_sr[0]
    i = 0
    while exsist_money > 0:
        if exsist_money < coin:
            coin = coin_list_sr[i]
        num = round(exsist_money // coin, 0)
        residue = round(exsist_money % coin, 2)
        # residue = float("%.2f" % (exsist_money % coin))
        coin_num.append((coin, num))
        exsist_money = residue
        i = i+1

    return coin_num


'''
2.求最大子数组之和问题：给定一个整数数组（数组元素有负有正），求其连续子数组之和的最大值。
'''


def array_sum(array):
    """
    对数组中的元素进行扫描，用this_sum记录扫描元素的和，从跟第一个元素开始扫描，this_sum不能小于0，如果小于0，
    那么 this_sum从新记录扫描元素的和(这个时候this_sum置为0)，
    如果this_sum不为0，那么就和max_sum比较（大于max_sum那就把this_sum的值给max_sum，不大于就不变）
    意思就是扫描到的最大和保存在max_sum中。
    """
    # arr_len = len(array)
    max_sum = 0
    this_sum = 0
    for i in array:
        this_sum = this_sum + array[i]
        if this_sum > max_sum:
            max_sum = this_sum
        elif this_sum < 0:
            this_sum = 0
    return max_sum


'''
3.一辆汽车加满油后可行驶n公里。旅途中有若干个加油站。设计一个有效算法，
指出应在哪些加油站停靠加油，使沿途加油次数最少。 对于给定的n(n <= 5000)和k(k <= 1000)个加油站位置，编程计算最少加油次数。
# 设汽车加满油后可行驶n公里，且旅途中有k个加油站.
'''


def oil_station(capacity, os_num, os_map):

    for k in os_map:
        if k > capacity:
            print('car can`t go')
            return False
    os_need = 0
    i = 0
    use = 0
    while i <= os_num:
        use = use + os_map[i]
        if use >= capacity:
            use = os_map[i]
            os_need = os_need + 1
        i = i + 1
    print('num', os_need)


def knapsak(BAG, vw_arr, record=0):

    v_w = list()
    l = len(vw_arr)
    for i in range(l):
        v_w.append((round(vw_arr[i][0]/vw_arr[i][1], 2), i))

    a = sorted(v_w)
    v_w = list(reversed(a))

    left = BAG

    for i in range(l):
        if vw_arr[v_w[i][1]][1] > left:
            print('no enough room.')
            print('put some of ', vw_arr[i], 'in bag:', left)

            break
        left = left - vw_arr[i][1]
        print('input ', vw_arr[i])


if __name__ == '__main__':
    print('input')
    BAG = 50
    M = 50
    w = [10, 30, 20, 5]
    v = [200, 400, 100, 10]
    vw_arr = [(x, y) for x, y in zip(v, w)]

    knapsak(BAG, vw_arr)

