from mining import Mining
from algorithms import Algorithms
class node:
    sizes = [57247,98732,134928,77275,29240,15440,70820,139603,63718,143807,190457,40572]
    fees=[0.0887,0.1856,0.2307,0.1522,0.0532,0.0250,0.1409,0.2541,0.1147,0.2660,0.2933,0.0686]
    print('sizes :{}'.format(sum(sizes)))
    Algorithms.theSort(sizes)

    # m = Mining(sizes)
    # m.addTransactionsToBlock()



    