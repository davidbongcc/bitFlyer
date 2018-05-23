
from algorithms import Algorithms
from transaction import Transaction
from blockchain import Blockchain
class node:
    # sizes = [57247,98732,134928,77275,29240,15440,70820,139603,63718,143807,190457,40572]
    # fees=[0.0887,0.1856,0.2307,0.1522,0.0532,0.0250,0.1409,0.2541,0.1147,0.2660,0.2933,0.0686]
    # print('sizes :{}'.format(sum(sizes)))
    # algo = Algorithms(sizes)
    # algo.runSort()

    # # m = Mining(sizes)
    # # m.addTransactionsToBlock()






    def __init__(self):
        self.__transactions = []
        self.__transactions.append(Transaction(57247,0.0887,1))
        self.__transactions.append(Transaction(98732,0.1856,2))
        self.__transactions.append(Transaction(134928,0.2307,3))
        self.__transactions.append(Transaction(77275,0.1522,4))
        self.__transactions.append(Transaction(29240,0.0532,5))
        self.__transactions.append(Transaction(15440,0.0250,6))
        self.__transactions.append(Transaction(70820,0.1409,7))
        self.__transactions.append(Transaction(139603,0.2541,8))
        self.__transactions.append(Transaction(63718,0.1147,9))
        self.__transactions.append(Transaction(143807,0.2660,10))
        self.__transactions.append(Transaction(190457,0.2933,11))
        self.__transactions.append(Transaction(40572,0.686,12))
        bc = Blockchain(self.__transactions)
        # bc.mine_transaction()


       
    # # def addTransaction(self):
    # #     self.__transactions.append(Transaction(57247,0.0887,1))
    # #     self.__transactions.append(Transaction(98732,0.1856,2))
    # #     self.__transactions.append(Transaction(134928,0.2307,3))
    # #     self.__transactions.append(Transaction(77275,0.1522,4))
    # #     self.__transactions.append(Transaction(29240,0.0532,5))
    # #     self.__transactions.append(Transaction(15440,0.0250,6))
    # #     self.__transactions.append(Transaction(70820,0.1409,7))
    # #     self.__transactions.append(Transaction(139603,0.2541,8))
    # #     self.__transactions.append(Transaction(63718,0.1147,9))
    # #     self.__transactions.append(Transaction(143807,0.2660,10))
    # #     self.__transactions.append(Transaction(190457,0.2933,11))
    # #     self.__transactions.append(Transaction(40572,0.686,12))
        