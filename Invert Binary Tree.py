# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    @classmethod
    def invertTree(cls, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            left = cls.invertTree(root.left)
            right = cls.invertTree(root.right)
            root.left = right
            root.right = left
            return root
