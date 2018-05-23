from transaction import Transaction
from block import Block
from blockchain import Blockchain
class Main:

    # transactions = []
    # transactions.append(Transaction(57247,0.0887,1))
    # transactions.append(Transaction(98732,0.1856,2))
    # transactions.append(Transaction(134928,0.2307,3))
    # transactions.append(Transaction(77275,0.1522,4))
    # transactions.append(Transaction(29240,0.0532,5))
    # transactions.append(Transaction(15440,0.0250,6))
    # transactions.append(Transaction(70820,0.1409,7))
    # transactions.append(Transaction(139603,0.2541,8))
    # transactions.append(Transaction(63718,0.1147,9))
    # transactions.append(Transaction(143807,0.2660,10))
    # transactions.append(Transaction(190457,0.2933,11))
    transactions.append(Transaction(40572,0.686,12))
    sizes = [57247,98732,134928,77275,29240,15440,70820,139603,63718,143807,190457,40572]
    fees=[0.0887,0.1856,0.2307,0.1522,0.0532,0.0250,0.1409,0.2541,0.1147,0.2660,0.2933,0.0686]
    sizes.sort(reverse=True)
    fees.sort(reverse=True)
    print(sizes)
    print(fees)
    # bc = Blockchain(transactions)
    # print(bc.mine_transaction())
    

 
        