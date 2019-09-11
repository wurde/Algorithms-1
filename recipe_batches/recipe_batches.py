#!/usr/bin/python

#
# Dependencies
#

import math

#
# Define method
#

def recipe_batches(recipe, ingredients):
  counts = []

  for name,value in recipe.items():
    if name in ingredients:
      counts.append(math.floor(ingredients[name] / value))
    else:
      counts.append(0)

  max_batches = max(counts)

  for count in counts:
    if count < max_batches:
      max_batches = count

  return max_batches

#
# Execute method
#

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
