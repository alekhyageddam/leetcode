# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #1. Two Runner Technique: One fast and one slow, at any given point, the fast runner will be 2x as ahead of slow runner. F -> 2 nodes/iteration 2-> 1 node/iteration
        
        # Reverse the 2nd half of the linked lists
        # Compare 1st half to reverse of 2nd half
        # O(n) time | O(1) space
        
        
        #2. Brute Force approach, reverse the list and check if L = Reverse(L)
        
        result = []
        temp = head
        while temp is not None:
            result.append(temp.val)
            temp = temp.next 
        check = True if result == reversed(result) else False
        print(check)
        if result == result[::-1]:
            return True
        return False