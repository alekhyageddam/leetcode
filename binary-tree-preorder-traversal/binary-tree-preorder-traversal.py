# Definition for a binary tree node.
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        order, stack = [], [root]
        while stack:
            node = stack.pop()
            order.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return order