# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p and q:
            if p.left is None and p.right is None and q.left is None and q.right is None:
                return p.val == q.val

            if p.left and q.left:
                return self.isSameTree(p.left, q.left)
            else:
                return False

            if p.right and q.right:
                return self.isSameTree(p.right, q.right)
            else:
                return False
