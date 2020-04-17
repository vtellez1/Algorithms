#!/usr/bin/python

import sys


def making_change(amount, denominations):
    # initialize a cache as a list of 0s with a length equal to amount we're looking to make change for.
    cache = [0 for i in range(amount + 1)]
    # Since we know there is one way to make 0 cents in change, we'll initialize:
    cache[0] = 1

    for coin in denominations:
      # for a given coin, we can loop through all of the higher amounts between our coin and the amount
      # (i.e., for higher_amount in range(coin, amount + 1))
        for higher_amount in range(coin, amount + 1):
          # If we take the difference between the higher amount and the value of our coin,
          #  we can start building up the values in our cache.
            cache[higher_amount] = cache[higher_amount] + cache[amount - coin]

    return cache[amount]


denominations = [1, 5, 10, 25, 50]
print(making_change(5, denominations))

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
