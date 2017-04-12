class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = range(1, len(nums)+1)
        Set = set(nums)
        result = []
        for num in arr:
            if num not in Set:
                result.append(num)
        return result

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
