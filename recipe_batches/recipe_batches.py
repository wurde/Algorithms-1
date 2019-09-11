#!/usr/bin/python

#
# Dependencies
#

import math

#
# Define method
#

def recipe_batches(recipe, ingredients):
  pass 
  # TODO define counts = [] * len(recipe)
  # TODO iterate over recipe
    # TODO divide inventory by required amounts
    # TODO set value in counts array (preserve index)
  # TODO set max_batches = max(counts)
  # TODO iterate over counts
    # TODO if count < max_batch
    # TODO set max_batches = count

#
# Execute method
#

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
