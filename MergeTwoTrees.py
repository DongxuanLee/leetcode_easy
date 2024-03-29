# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return
        elif not t1 and t2:
            return t2
        elif not t2 and t1:
            return t1
        if t1.left and t2.left:
            self.mergeTrees(t1.left,t2.left)
        if t1.right and t2.right:
            self.mergeTrees(t1.right, t2.right)
        t1.val = t1.val+t2.val
        if t2.left and not t1.left:
            t1.left = t2.left
        if t2.right and not t1.right:
            t1.right = t2.right
        return t1
        
