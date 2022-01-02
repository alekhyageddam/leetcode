# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if list has no nodes or only one node left
        if not head or not head.next:
            return head
        
        #nodes to be swapped
        first_node = head
        second_node = head.next 
        
        #swap
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        
        #now head is the second node
        return second_node