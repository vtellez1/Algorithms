#!/usr/bin/python

# function to generate all of the possible plays that can be made in a game of "Rock Paper Scissors"
# Your output should be: a list of lists containing strings.
#   Each inner list should have length equal to the input n.

# * You'll want to define a list with all of the possible Rock Paper Scissors plays.
# * The problem asks to generate a bunch of permutations, so we're probably going to want to opt for using recursion again.
#   Since we're building up a list of results, we'll have to pass the list we're constructing around to multiple recursive
#   calls so that each recursive call can add to the overall result. However, the tests only give our function `n` as input.
#   To get around this, we could define an inner recursive helper function that will perform the recursion for us,
#   while allowing us to preserve the outer function's function signature.

# * In Python, you can concatenate two lists with the `+` operator.
#   However, you'll want to make sure that both operands are lists!

# * If you opt to define an inner recursive helper function,
#   don't forget to make an initial call to the recursive helper function to kick off the recursion.

import sys
"""
(0)
------------
[[]]

(1)
------------
[['rock'], ['paper'], ['scissors']]

(2)
-------------
[['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'],
 ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], 
 ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

 (3)
 ------------
[['rock', 'rock', 'rock'], ['rock', 'rock', 'paper'], ['rock', 'rock', 'scissors'],
 ['rock', 'paper', 'rock'], ['rock', 'paper', 'paper'], ['rock', 'paper', 'scissors'],
 ['rock', 'scissors', 'rock'], ['rock', 'scissors', 'paper'], ['rock', 'scissors', 'scissors'],
 ['paper', 'rock', 'rock'], ['paper', 'rock', 'paper'], ['paper', 'rock', 'scissors'],
 ['paper', 'paper', 'rock'], ['paper', 'paper', 'paper'], ['paper', 'paper', 'scissors'],
 ['paper', 'scissors', 'rock'], ['paper', 'scissors', 'paper'], ['paper', 'scissors', 'scissors'],
 ['scissors', 'rock', 'rock'], ['scissors', 'rock', 'paper'], ['scissors', 'rock', 'scissors'],
 ['scissors', 'paper', 'rock'], ['scissors', 'paper', 'paper'], ['scissors', 'paper', 'scissors'],
 ['scissors', 'scissors', 'rock'], ['scissors', 'scissors', 'paper'], ['scissors', 'scissors', 'scissors']

"""


def rock_paper_scissors(n):
    output = []
    rps = [['rock'], ['paper'], ['scissors']]

    if n <= 0:
        return [[]]
    if n == 1:
        return rps
    else:
        for i in rock_paper_scissors(n-1):
            for j in rps:
                output.append(i + j)
    return output


print(rock_paper_scissors(3))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
