class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.queue = []
        self.head = -1
        self.tail = -1
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        #if queue is full, return false
        if self.isFull():
            return False
        
        
        #enqueue : move head if it is empty queue
        if self.isEmpty():
            self.head=0
            
        #if queue is not full, check whether tail is at k
        self.tail = (self.tail+1)%self.size
        
        if len(self.queue)<self.size:
            self.queue.insert(self.tail, value)
        else:
            self.queue[self.tail]=value
        print("enQueue: ",self.queue, self.head, self.tail, "val=", value)
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            print("deQueue: ",self.queue, self.head, self.tail)
            return False
        if self.tail==self.head:
            self.tail=-1
            self.head=-1
            print("deQueue: ",self.queue, self.head, self.tail)
            return True
        #move to front
        self.head = (self.head+1)%self.size
        print("deQueue: ",self.queue, self.head, self.tail)
        return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[self.head]
        else:
            return -1


    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[self.tail]
        else:
            return -1
        
    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if (self.head==-1):
            return True
        else:
            return False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if (((self.tail+1)%self.size)==self.head):
            return True
        else:
            return False
        
if __name__ == '__main__':
    myList = ["null"]

#     k=6
#     obj = MyCircularQueue(k)
#     param_1 = obj.enQueue(3)
#     param_2 = obj.enQueue(1)
#     param_3 = obj.enQueue(2)
#     param_4 = obj.enQueue(3)
#     param_5 = obj.enQueue(4)
#     param_6 = obj.Rear()
#     param_7 = obj.isFull()
#     param_8 = obj.deQueue()
#     param_9 = obj.enQueue(4)
#     param_10 = obj.Rear()

    k=6
    obj = MyCircularQueue(k)
    
    param_1 = obj.enQueue(6)
    param_2 = obj.Rear()
    param_3 = obj.Rear()
    param_4 = obj.deQueue()
    param_5 = obj.enQueue(5)
    param_6 = obj.Rear()
    param_7 = obj.deQueue()
    param_8 = obj.Front()
    param_9 = obj.deQueue()
    param_10 = obj.deQueue()
    param_11 = obj.deQueue()
    
    myList.append(param_1)
    myList.append(param_2)
    myList.append(param_3)
    myList.append(param_4)
    myList.append(param_5)
    myList.append(param_6)
    myList.append(param_7)
    myList.append(param_8)
    myList.append(param_9)
    myList.append(param_10)
    param_11 = obj.deQueue()
    print(myList)

    
    