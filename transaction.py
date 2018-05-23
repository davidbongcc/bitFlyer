#Transaction class object
class Transaction:
    def __init__(self,size=0,fee=0,index=0):
        self.index = index
        self.size = size
        self.fee = fee
