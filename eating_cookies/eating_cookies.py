#!/usr/bin/python

#
# Dependencies
#

import sys

#
# Define method
#

def eating_cookies(n, cache=None):
  # Define base case
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif n == 1:
    return 1

  # Define recursion case
  return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)

# 
# Execute method
# 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
