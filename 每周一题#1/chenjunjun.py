#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

    0 <= amount <= 5000
    1 <= coin <= 5000
    the number of coins is less than 500
    the answer is guaranteed to fit into signed 32-bit integer

Example 1:

    Input: amount = 5, coins = [1, 2, 5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1

Example 2:

    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

    Input: amount = 10, coins = [10]
    Output: 1

"""
import sys


def jie(amount, coins, result, cb):
    """递归求值

    计算从coins中的硬币组合符合值amount的方案

    :param amount: 目标总额
    :type amount: int
    :param coins: 可选的硬币种类
    :type coins: list
    :param result: 已经选择的硬币
    :type result: list
    :param cb: 回调,递归结束之后用于计算计算最终结果是否符合要求
    :return: None
    """
    if not coins:
        cb(result)
        return

    select_coin = coins[0]
    max_number = amount//select_coin
    for number in range(max_number + 1):
        new_result = result[:]
        new_result.append(number)
        jie(amount-number*select_coin, coins[1:], new_result, cb)


def ji_suan(amount, coins):
    """程序核心

    用于计算题目

    :param amount: 目标值
    :type amount: int
    :param coins:可选的硬币种类
    :type coins: list
    :return: None
    """
    coins.sort(reverse=True)
    results = []

    def cb(result):
        current_amount = sum([r*c for r, c in zip(result, coins)])
        if amount == current_amount:
            results.append(result)

    jie(amount, coins, [], cb)
    return len(results)


if __name__ == "__main__":
    amount = int(sys.argv[1])
    coins = [int(x) for x in sys.argv[2:]]
    coins = list(set(coins))

    print ji_suan(amount, coins)
