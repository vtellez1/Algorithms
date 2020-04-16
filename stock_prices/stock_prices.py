#!/usr/bin/python

import argparse

# prices is a a list of stock prices.

# Your function should return the maximum profit that can be made from a single buy and sell.
# You must buy first before selling; no shorting is allowed here.

# For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530,
# which is the maximum profit that can be made from a single buy and then sell of these stock prices.

# For this problem, we essentially want to:
# find the maximum difference between the smallest and largest prices in the list of prices,

# but we also have to make sure:
#  that the max profit is computed by subtracting some price by another price that comes _before_ it;
# it can't come after it in the list of prices.

# So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`?


def find_max_profit(prices):
    max_profit_so_far = prices[1] - prices[0]

    for i in range(0, len(prices)):
        for x in range(1, len(prices)):
            if x > i:
                if prices[x] - prices[i] > max_profit_so_far:
                    max_profit_so_far = prices[x] - prices[i]

    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
