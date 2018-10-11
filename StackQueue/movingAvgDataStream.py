'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.list = []
        self.size= size
        self.index = -1

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.index = (self.index+1)%self.size
        if len(self.list)<self.size:
            self.list.insert(self.index, val)
        else:
            self.list[self.index]=val
        #if -ends
        return self.getSum()/len(self.list)
    
    def getSum(self):
        sum=0
        for i in self.list:
            sum+=i
        #for -ends
        return sum
    
if __name__ == '__main__':
    size=3
    obj = MovingAverage(size)
    param_1 = obj.next(1)
    param_2 = obj.next(10)
    param_3 = obj.next(3)
    param_4 = obj.next(5)
    
    myList = [param_1, param_2, param_3, param_4]
    print(myList)