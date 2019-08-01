# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
    def invertTree2(self,root):
        if not root:
            return None
        quee = []
        quee.append(root)
        while quee:
            x = quee.pop()
            tmp = x.left
            x.left = x.right
            x.right = tmp
            if x.left:
                quee.append(x.left)
            if x.right:
                quee.append(x.right)
        return root