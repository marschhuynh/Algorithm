class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        result = max
        for num in nums:
            if num:
                max += 1
                if max > result:
                    result = max
            else:
                max = 0
        return result


print(Solution().findMaxConsecutiveOnes([1]))
