# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root is not None:
            stack.append((1,root))
        
        depth = 0
        while len(stack) > 0:
            current_depth, root = stack.pop()
            if root:
                depth = max(current_depth, depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth