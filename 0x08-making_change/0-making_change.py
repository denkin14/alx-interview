#!/usr/bin/python3


def makeChange(coins, total):
    # Initialize table
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Fill table
    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Return result
    return min_coins[total] if min_coins[total] != float('inf') else -1
