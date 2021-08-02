# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
     #recursive solution, O(n+m) space and time 
        # if l1 is None and l2 is None:
        #     return None
        # if l1 is None:
        #     return l2
        # elif l2 is None:
        #     return l1
        # elif l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(ll.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
        
     #iterative solution
        prehead = ListNode(-1)
        
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next 
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
            
        prev.next = l1 if l1 is not None else l2
        
        return prehead.next
        
    
    