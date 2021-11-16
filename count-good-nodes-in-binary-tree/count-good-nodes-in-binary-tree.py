# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float("-inf"))]
        goodNode_count = 0
        
        while stack:
            node, current_max = stack.pop()
            if node.val >= current_max:
                goodNode_count += 1
            if node.left:
                stack.append((node.left, max(node.val, current_max)))
            if node.right:
                stack.append((node.right, max(node.val, current_max)))
        
        return goodNode_count