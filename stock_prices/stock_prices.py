#!/usr/bin/python

#
# Dependencies
#

import argparse

#
# Define method
#

def find_max_profit(prices):
  lowest_price = prices.pop()

  for price in prices:
    if price < lowest_price:
      lowest_price = price

  return lowest_price

#
# Execute method
#

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))