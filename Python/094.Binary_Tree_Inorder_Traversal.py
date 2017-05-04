# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self,root,arr):
        if root.left:
            self.inorder(root.left,arr)
        arr.append(root.val)
        if root.right:  
            self.inorder(root.right,arr)
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            arr = []
            self.inorder(root,arr)
            return arr
        else:
            return []