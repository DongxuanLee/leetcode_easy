# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # self.diameter = []
        self.maxdiame = 0
        self.finddiame(root)
        # return max(self.diameter)
        return self.maxdiame

    def finddiame(self, node):
        if not node:
            return 0
        leftlegth = 0
        rightlegth = 0
        if node.left:
            leftlegth = self.finddiame(node.left) + 1

        if node.right:
            rightlegth = self.finddiame(node.right) + 1
        self.maxdiame = max(leftlegth+rightlegth,self.maxdiame)

        return max(leftlegth+1,rightlegth+1)


