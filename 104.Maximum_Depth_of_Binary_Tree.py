# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            left = 1
            right = 1
            if root.left:
                left = 1 + self.maxDepth(root.left)
            if root.right:
                right = 1 + self.maxDepth(root.right)
            return max(left, right)
        else:
            return 0