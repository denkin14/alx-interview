#!/usr/bin/python3
"""
Making change task
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coins_needed = 0
    for coin in coins:
        if total / coin > 0:
            coins_needed = coins_needed + (total // coin)
            total = total % coin

    if total != 0 or coins_needed == 0:
        return -1
    return coins_needed
