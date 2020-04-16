#!/usr/bin/python
"""
Function receives: recipe in the form of a dictionary, as well as all of the ingredients you have available also dictionary form.

Keys=ingredient names, values = amounts.

In the case of the recipe dictionary, these amounts will represent the amount of each ingredient needed for the recipe,
 while in the case of the ingredients dictionary, the amounts represent the amounts available to you.

Function should output: maximum number of whole batches that can be made.

 #* What's the _minimum_ number of loops we need to perform in order to write a working implementation?
"""
import math


def recipe_batches(recipe, ingredients):
    amt = []

    for i in recipe:
        if i in ingredients:
            amt.append(ingredients[i] // recipe[i])
        else:
            amt.append(0)
    max_batches = min(amt)
    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
