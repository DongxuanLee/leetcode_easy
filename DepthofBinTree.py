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
        if not root:
            return 0
        left_depth =self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        if left_depth>=right_depth:
            return left_depth+1
        else:
            return right_depth+1

# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
#         self.left_depth =self.maxDepth(root.left)
#         self.right_depth = self.maxDepth(root.right)
#         if self.left_depth>=self.right_depth:
#             return self.left_depth+1
#         else:
#             return self.right_depth+1
