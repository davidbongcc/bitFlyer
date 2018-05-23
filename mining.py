# define a function to find the maxium reward using the provided transactions.
# o(n^2)

import sys
from transaction import Transaction

class Mining:

    # print('sizes :{}'.format(sizes))
    # print('fees :{}'.format(sizes))
    def __init__(self,data):
        print('constructor')
        for a in data:
            total = 0
            total += a
            print(total)

    def addTransactionsToBlock(self):
        print('add transactions to block')