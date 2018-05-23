# Sorting 
class Algorithms:

    def __init__(self):
        pass

    @staticmethod
    def theSort(data):
        i = 0
        j = len(data) -1
        p = int(i+j/2)
        pivot = data[p]
        print(int(pivot))
        left = 0
        right = len(data) -1

        while True:
            if(i>=j):
                break
            while True:
                if((data[i]<pivot) and (i < right)):
                    i+=1
                else:
                    break
            
            while True:
                if((pivot < data[j]) and (j > left):
                    j-=1
                else:
                    break

        

