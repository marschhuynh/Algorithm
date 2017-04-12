# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    @classmethod
    def maxDepth(cls, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return max(cls.maxDepth(root.left), cls.maxDepth(root.right)) + 1
        else:
            return 0

print(Solution().maxDepth(None))
