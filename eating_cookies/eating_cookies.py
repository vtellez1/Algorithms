#!/usr/bin/python

import sys
# Cookie Monster can eat either 0, 1, 2, or 3 cookies at a time.
# Implement a function `eating_cookies` that counts the number of possible ways
# Cookie Monster can eat all of the cookies in the jar.

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

"""
def eating_cookies(n, cache=None):
    # if 1 or less cookies (0 or negative), only 1 way to eat it.
    if n <= 1:
        return 1
    if n == 2:
        return 2
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
--------------------------------------

(1)
--------------
1

(2)
---------------
1  1
2

(3)
---------------
1  11
1   2
21
3

(4)
----------------
1 111
1  12
1  21
1   3
211
22
31

(5)
----------------
1     1111
1      112
1      121
1       13
1      211
1       22
1       31
2111
221
212
23
311
32

"""


def eating_cookies(n, cache=None):
    if cache is None:
        cache = [0] * (n + 1)
    if n <= 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    elif cache[n] == 0:
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
