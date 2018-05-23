from block import Block
from transaction import Transaction



class Blockchain:

    def __init__(self, transactions):
        
        self.transactions = transactions
    
    #This should returns a Tuple the size with the fee
    def mine_transaction(self):
        return self.transactions[:]
            