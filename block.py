from time import time

from printable import Printable

class Block(Printable):
    def __init__(self, index,transactions ,time=time()):
        self.index = index
        self.timestamp = time
        self.transactions = transactions



