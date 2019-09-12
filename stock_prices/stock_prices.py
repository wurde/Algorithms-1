#!/usr/bin/python

#
# Dependencies
#

import argparse

#
# Define method
#

def find_max_profit(prices):
  profit = None

  for i in range(0, len(prices)):
    for j in range(i+1, len(prices)):
      buy_price = prices[i]
      sell_price = prices[j]

      if profit == None:
        profit = sell_price - buy_price
      elif (sell_price - buy_price) > profit:
        profit = sell_price - buy_price

  return profit

#
# Execute method
#

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
  