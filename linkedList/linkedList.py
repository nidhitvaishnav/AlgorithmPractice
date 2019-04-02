from node import Node
class LinkedList:
    def __init__(self):
        self.head = None
    
    def lengthofList(self):
        node = self.head
        count = 0
        while(node!=None):
            count+=1
            node = node.next
        #whie -ends
        return count
        
    def traverseList(self):
        node = self.head
        while(node!=None):
            print(node.data, end=" ")
            if node.next!=None:
                print("->", end=" ")
            node = node.next
        #while -ends
        print()
    
    def reverseLinkedList(self, node):
        if(node.next!=None):
            self.reverseLinkedList(node.next)
        if node.next!=None:
            print("->", end=" ")
        print(node.data, end=" ")
    
    def findPreviousNode(self, node):
        currNode = self.head
        while(currNode.next!=None):
            if (currNode.next==node):
                return currNode
            else:
                currNode = currNode.next
            #if -ends
        #while -ends
        return None
    
    
    def insert(self, data):
        node = Node(data)
        current = self.head
        while(current.next!=None):
            current = current.next
        #while -ends
        current.next = node
    
    def insertAtBegining(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def insertAfter(self, currNode, data):
        added = Node(data)
        added.next = currNode.next
        currNode.next = added
        
    def insertBefore(self, node, data):
        prevNode = self.findPreviousNode(node)
        newNode = Node(data)
        newNode.next = node
        prevNode.next = newNode
        
    def insertAtIndex(self, index, data):
        '''Index starts from 0'''
        len = self.lengthofList()
        if index<0 or index>len:
            print("Error: index out of bound Error")
        elif index==0:
            self.insertAtBegining(data)
        elif index==len:
            self.insert(data)
        else:
            node = Node(data)
            currNode = self.head
            prevNode=None
            i = 0
            while(currNode!=None):
                if (index==i):
                    node.next = currNode
                    prevNode.next = node
                    return
                else:
                    i+=1
                    prevNode=currNode
                    currNode = currNode.next
                #if else -ends
            #while -ends
        #if-elif-else -ends
                            
    
    def deleteAtEnd(self):
        curr = self.head
        prev = None
        while(curr.next!=None):
            prev = curr
            curr = curr.next
        #while -ends
        prev.next = None
    
    def deleteAtBegin(self):
        self.head = self.head.next
        
    def deleteKey(self, data):
        if self.head.data==data:
            self.deleteAtBegin()
        else:
            currNode = self.head
            prevNode = None
            while(currNode!=None):
                if currNode.data==data:
                    prevNode.next = currNode.next
                    return
                else:
                    prevNode = currNode
                    currNode = currNode.next
                #if -ends
            #while -ends
        #else -ends
        
    def deleteAtIndex(self, index):
        '''Index starts from 0'''
        len = self.lengthofList()
        if index<0 or index>=len:
            print("Error: index out of bound Error")
        elif index==0:
            self.deleteAtBegin()
        elif (index==(len-1)):
            self.deleteAtEnd()
        else:
            currNode = self.head
            prevNode=None
            i = 0
            while(currNode!=None):
                if (index==i):
                    prevNode.next = currNode.next
                    return
                else:
                    i+=1
                    prevNode=currNode
                    currNode = currNode.next
                #if else -ends
            #while -ends
        #if-elif-else -ends
        
    def deleteLinkedList(self):
        self.head=None