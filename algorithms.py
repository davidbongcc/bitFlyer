# Sorting 
class Algorithms:

    def __init__(self,data):
        self.data = data

    def runSort(self):
        self.theSort(self.data,0,len(self.data)-1)
        print(self.data)

    
    def theSort(self,x,left,right):
        i = left
        j = right
        p = int(i+j/2)
        pivot = x[p]
        temp =0
        # print(int(pivot))
 

        while True:
            
            while True:
                if((x[i]<pivot) and (i < right)):
                    i+=1
                else:
                    break
            
            while True:
                if((pivot < x[j]) and (j > left)):
                    j-=1
                else:
                    break
            if(i<=j):
                temp=x[i]
                x[i] =x[j]
                x[j] =temp
                i+=1
                j-=1

            if((i>j)or (i==j)):
                break
        
        if(left < j):
            self.theSort(x,left,j)
        if(i < right):
            self.theSort(x,i,right)

        

        

