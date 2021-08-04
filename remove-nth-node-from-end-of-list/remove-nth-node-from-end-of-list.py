# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        second = head
        counter = 1
        
        while counter <= n:
            second = second.next
            counter += 1
        
        if second is None:
            head = head.next
            return head
            
        while second.next is not None:
            second = second.next
            first = first.next
            
        first.next = first.next.next
        return head