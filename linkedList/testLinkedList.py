from linkedList import LinkedList
from node import Node

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    llist.head.next = second
    second.next = third
    
    #testing linkedList
    llist.traverseList()
    print("length of list:",llist.lengthofList())
    llist.insert(4)
    llist.traverseList()
    
    llist.reverseLinkedList(llist.head)
    print()
    llist.insertAtBegining(0)
    llist.traverseList()
    llist.deleteAtEnd()
    llist.traverseList()
    llist.deleteAtBegin()
    llist.traverseList()
    
    llist.insertAfter(currNode=second, data=10)
    llist.traverseList()
    print(llist.findPreviousNode(node=third).data)
    llist.insertBefore(node=second, data=100)
    llist.traverseList()
    llist.insertAtIndex(index=3, data=55)
    llist.traverseList()
    llist.deleteKey(data=100)
    llist.traverseList()
    llist.deleteAtIndex(index=3)
    llist.traverseList()
    

    
    
    