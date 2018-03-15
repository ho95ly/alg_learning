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
        coin_num.append((coin, num))
        exsist_money = residue
        i = i+1

    return coin_num


if __name__ == '__main__':
    coin_list = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1]
    price = 1.48
    give_money = 5
    coin_num = give_change(coin_list, price, give_money)
    for i in coin_num:
        print(i)