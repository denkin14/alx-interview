#!/usr/bin/python3
"""
Prime numbers Game
"""

def primeNumbers(n):
    """will return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary. lower boundary is always 1
    """
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos


def isWinner(x, nums):
    """
    will determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Returns:
        Name of winner (Maria or Ben) or Not if winner wont be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNos = primeNumbers(nums[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
