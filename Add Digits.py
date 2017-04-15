class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return num - 9*((num-1)/9)

print(Solution().addDigits(0))
