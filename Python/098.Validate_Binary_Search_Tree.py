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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            arr = []
            self.inorder(root,arr)
            for i in range(1,len(arr)):
                if arr[i-1] >= arr[i]:
                    return False
            return True
        return True