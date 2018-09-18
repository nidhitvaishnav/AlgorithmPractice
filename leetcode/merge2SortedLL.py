# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tail = ListNode(None)
        while l1 and l2:
            if l1.val<=l2.val:
                tail.next, tail, l1 = l1, l1, l1.next
            else:
                tail.next, tail, l2 = l2, l2, l2.next
            #if -ends
        #while -ends
        tail.next = (l1 or l2) if (l1 or l2) else None
        return head.next
            
if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(4)
    l2 = ListNode(1)
    l2.next=ListNode(3)
    l2.next.next=ListNode(4)
 
    solution = Solution()
    mergedList = solution.mergeTwoLists(l1, l2)
    for i in range(6):
        print(mergedList.val)
        mergedList = mergedList.next