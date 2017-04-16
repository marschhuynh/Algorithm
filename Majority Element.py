class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        d = {}
        for i in nums:
            try:
                d[i] += 1
            except:
                d[i] = 1
        for i in nums:
            if d[i] > n / 2:
                return i
