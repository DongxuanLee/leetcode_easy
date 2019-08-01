# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        node = self.sumBest(root)
        return node
    def sumBest(self,node):
        if not node:
            return
        if node.right:
            self.sumBest(node.right)
        self.sum =self.sum +node.val
        node.val = self.sum
        if node.left:
            self.sumBest(node.left)
        return node

