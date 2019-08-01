# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        self.pathSumRe1(root,sum,[sum])
        return self.count
    def pathSumRe1(self,node,sum,target):
        if not node:
            return 0
        for i in target:
            if i - node.val ==0:
                self.count += 1
        target = [t - node.val for t in target] + [sum]
        self.pathSumRe1(node.left,sum,target)
        self.pathSumRe1(node.right, sum,target)
    def pathSumRe(self,node,sum):
        if not node:
            return 0
        self.path(node,sum)
        self.pathSumRe(node.left,sum)
        self.pathSumRe(node.right,sum)
    def path(self,node,sum):
        if not node:
            return 0
        if sum - node.val == 0:
            self.count +=1
        self.path(node.left,sum-node.val)
        self.path(node.right,sum-node.val)
